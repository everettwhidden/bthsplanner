import reflex as rx

from data.courses import COURSE_CATALOG, MAJORS, double_alternates

from .catalog_search import search_electives
from .constants import SENIOR_GOV_COURSES
from .export import build_plan_xlsx
from .helpers import (
    build_partner_map,
    calculate_total_periods,
    grade_badges,
    next_lang_level,
)

    
class PlannerState(rx.State):
    active_tab: str = "Plan"
    sidebar_open: bool = True


    pre_credits: dict[str, bool] = {
        "Algebra I": False,
        "Geometry": False,
        "US History" : False,
        "Biology/Living Environment" : False,
    }
    

    partner_map: dict[str, str] =build_partner_map(double_alternates)

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_pre_credit(self, credit: str, checked: bool):
        snapshot = self._export_progress_dict()
        self.pre_credits[credit] = checked
        if credit == "Geometry":
            if checked:
        
                self.j_math = "AP Calculus BC"
                self.sn_math = "Multivariable Calculus"
            else:
                self.j_math = "Pre-Calculus"
                self.sn_math = "AP Calculus BC"
        if credit == "US History":
            if checked:
                if self.major == "Finance":
                    self.j_his = "Participation in Government"
                else:
                    self.j_his = "Economics"
                    
            elif self.j_his == "Economics":
                self.j_his = "Regents US History"
            elif self.j_his == "Participation in Government":
                self.j_his = "Regents US History"
            else:
                self.j_his = "Regents US History"
        if credit == "Language":
            if checked:
                self.f_lang = next_lang_level(self.pre_language)
            else:
                self.f_lang = self.pre_language
            self.sync_so_eng_for_language()
        if credit in ("Biology/Living Environment", "Algebra I"):
            self.sync_f_sci()
        self._enforce_ap_limits()
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    pre_language: str = "Spanish I"

    def change_pre_language(self, val: str):
        self.pre_language = val
        if self.pre_credits.get("Language", False):
            self.f_lang = next_lang_level(val)
        else:
            self.f_lang = val

    
    def sync_f_sci(self):
        has_bio = self.pre_credits.get("Biology/Living Environment", False)
        
        if not has_bio:
            self.f_sci = "Regents Biology"
        else:
            self.f_sci = "Regents Physics"

    def _default_j_his(self) -> str:
        # what junior history should default to, based on the US History credit
        if not self.pre_credits.get("US History", False):
            return "Regents US History"
        if self.major == "Finance" or self.has_econ_gov_conflict:
            return "Participation in Government"
        return "Economics"

    def _default_f_sci(self) -> str:
        if not self.pre_credits.get("Biology/Living Environment", False):
            return "Regents Biology"
        else:
            return self.f_sci

    def sync_so_eng_for_language(self):
        if self.sophomore_ap_count > 3 and self.so_eng == "AP Capstone Seminar":
            self.so_eng = "English 10"

    

    def change_tab(self, name: str):
        self.active_tab = name
    #initial courses and major
    major: str = "Aerospace Engineering"
    f_hist: str = "Pre-AP World History"
    f_sci: str = "Regents Biology"
    f_math: str = "Geometry"
    f_lang: str = "Spanish I"
    so_eng: str = "English 10"
    so_hist: str = "AP European History"
    j_eng: str = "English 11"
    j_his: str = "Regents US History"
    j_phys: str = "Regents Physics"
    j_math: str = "Pre-Calculus"
    sn_math: str = "AP Calculus BC"
    sn_math_active: bool = True
    sn_eng: str = "Creative Writing"
    sn_his: str = "Economics"
    sn_ec: str = "Economics"
    sn_gov: str = "Participation in Government"

    # elective tracking lists 
    freshman_electives: list[str] = []
    sophomore_electives: list[str] = []
    junior_electives: list[str] = []   
    senior_electives: list[str] = []   
    

    
        
    
    # import/export data functions

    def _export_progress_dict(self) -> dict:
        return {
            "major": self.major,
            "f_hist": self.f_hist, "f_sci": self.f_sci, "f_math": self.f_math, "f_lang": self.f_lang,
            "so_eng": self.so_eng, "so_hist": self.so_hist,
            "j_eng": self.j_eng, "j_his": self.j_his, "j_phys": self.j_phys, "j_math": self.j_math,
            "sn_eng": self.sn_eng, "sn_his": self.sn_his, "sn_ec": self.sn_ec, "sn_gov": self.sn_gov, "sn_math": self.sn_math,
            "freshman_electives": list(self.freshman_electives),
            "sophomore_electives": list(self.sophomore_electives),
            "junior_electives": list(self.junior_electives),
            "senior_electives": list(self.senior_electives),
        }

    def _import_progress_dict(self, data: dict):
        self.major = data.get("major", self.major)
        self.f_hist = data.get("f_hist", self.f_hist)
        self.f_sci = data.get("f_sci", self.f_sci)
        self.f_math = data.get("f_math", self.f_math)
        self.f_lang = data.get("f_lang", self.f_lang)
        self.so_eng = data.get("so_eng", self.so_eng)
        self.so_hist = data.get("so_hist", self.so_hist)
        self.j_eng = data.get("j_eng", self.j_eng)
        self.j_his = data.get("j_his", self.j_his)
        self.j_phys = data.get("j_phys", self.j_phys)
        self.j_math = data.get("j_math", self.j_math)
        self.sn_eng = data.get("sn_eng", self.sn_eng)
        self.sn_his = data.get("sn_his", self.sn_his)
        self.sn_ec = data.get("sn_ec", self.sn_ec)
        self.sn_gov = data.get("sn_gov", self.sn_gov)
        self.sn_math = data.get("sn_math", self.sn_math)
        self.freshman_electives = data.get("freshman_electives", [])
        self.sophomore_electives = data.get("sophomore_electives", [])
        self.junior_electives = data.get("junior_electives", [])
        self.senior_electives = data.get("senior_electives", [])


    #search and filter stuff

    search_query: str = ""             # Live search text string

    active_modal_course: dict = {}     # Holds the course info for detail popup
    is_detail_open: bool = False       # Controls the visibility of the global detail modal

    #adnvaced language courses electives, exclude spanish because it has advanced spanish so logic is different
    none_history_placeholders = {
    "None (free period, econ senior year)",
    "None (free period, econ junior year)",
    "None (free period, gov senior year)",
    "None (free period, gov junior year)",
}
    current_modal_grade: str = "Junior"
    
    @rx.var
    def current_page(self) -> str:
        return self.router.page.path
    
    def export_to_excel(self):
        years = ["Freshman", "Sophomore", "Junior", "Senior"]
        data = build_plan_xlsx(
            major=self.major,
            year_courses={y: sorted(self._courses_for_year(y)) for y in years},
            course_counts={
                "Freshman": self.freshman_course_count, "Sophomore": self.sophomore_course_count,
                "Junior": self.junior_course_count, "Senior": self.senior_course_count,
            },
            periods={
                "Freshman": self.freshman_periods, "Sophomore": self.sophomore_periods,
                "Junior": self.junior_periods, "Senior": self.senior_periods,
            },
            ap_counts={
                "Freshman": self.freshman_ap_count, "Sophomore": self.sophomore_ap_count,
                "Junior": self.junior_ap_count, "Senior": self.senior_ap_count,
            },
        )
        return rx.download(data=data, filename="brooklyn_tech_plan.xlsx")
    
    @rx.var
    def freshman_math_courses(self) -> list[str]:
        if self.math_is_accelerated:
            return ["Algebra II"]
        if not self.pre_credits.get("Algebra I", False):
            return ["Algebra I", "Geometry"]
        return ["Geometry"]
    
    def change_major(self, val: str):
        self.major = val
        # Reset all dropdowns and electives to defaults on major change
        self.f_hist = "Pre-AP World History"
        self.f_sci = self._default_f_sci()
        self.f_math = "Geometry"
        if self.pre_credits.get("Language", False):
            self.f_lang = next_lang_level(self.pre_language)
        else:
            self.f_lang = self.pre_language
        self.so_eng = self.so_eng
        self.so_hist = self.so_hist
        self.j_eng = "English 11"
        self.j_his = self._default_j_his() 
        self.j_phys = "Regents Physics"
        self.j_math = self.j_math if self.math_is_accelerated else "Pre-Calculus"
        self.sn_eng = "Creative Writing"
        self.sn_his = "Participation in Government" if self.has_econ_gov_conflict else "Economics"
        self.sn_ec = "Economics"
        self.sn_gov = "Participation in Government"
        self.freshman_electives = []
        self.sophomore_electives = []
        self.junior_electives = []
        self.senior_electives = []
        self.sn_math = "Multivariable Calculus" if self.math_is_accelerated else "AP Calculus BC"


    def change_f_hist(self, val: str):
        snapshot = self._export_progress_dict()
        self.f_hist = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    def change_f_sci(self, val: str):
        snapshot = self._export_progress_dict()
        self.f_sci = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_f_math(self, val: str):
        snapshot = self._export_progress_dict()
        self.f_math = val
        self._enforce_ap_limits()
        self._evict_duplicates()
        self.j_math = "AP Calculus BC"
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_f_lang(self, val: str):
        snapshot = self._export_progress_dict()
        self.f_lang = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_so_eng(self, val: str):
        snapshot = self._export_progress_dict()
        self.so_eng = val
        if val == "AP Capstone Seminar":
    
            if self.senior_ap_count < 3:
                self.sn_eng = "AP Capstone Research"
                if not self._enforce_period_limits():
                    self._import_progress_dict(snapshot)
        else:
            self.sn_eng = "Creative Writing"
            if not self._enforce_period_limits():
                self._import_progress_dict(snapshot)

    def change_so_hist(self, val: str):
        snapshot = self._export_progress_dict()
        self.so_hist = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    def change_j_his(self, val: str):
        snapshot = self._export_progress_dict()
        prev = self.j_his
        self.j_his = val
        prev_needed_senior_econ = prev in ("Economics", "None (free period, econ senior year)")
        prev_needed_senior_gov = prev in ("Participation in Government", "None (free period, gov senior year)")
        if val == "None (free period, econ senior year)" or (prev_needed_senior_econ and val != "Economics"):
            self.sn_his = "Economics"
            if "AP Macroeconomics with Government" in self.senior_electives:
                self.senior_electives.remove("AP Macroeconomics with Government")
        if val == "None (free period, gov senior year)" or (prev_needed_senior_gov and val != "Participation in Government"):
            self.sn_his = "Participation in Government" \
            
            if "AP US Government" in self.senior_electives:
                self.senior_electives.remove("AP US Government")
            if "AP Comparative Government" in self.senior_electives:
                self.senior_electives.remove("AP Comparative Government")

        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
            if not self._enforce_period_limits():
                self._import_progress_dict(snapshot)

    def change_j_phys(self, val: str):
        snapshot = self._export_progress_dict()
        self.j_phys = val
        self._enforce_ap_limits()
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    def change_j_math(self, val: str):
        snapshot = self._export_progress_dict()
        self.j_math = val
        if val == "AP Calculus BC":
            self.sn_math = "Multivariable Calculus"
        if val == "Pre-Calculus":
            self.sn_math = "AP Calculus BC"
        self._enforce_ap_limits()
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    def change_sn_math(self, val: str):
        snapshot = self._export_progress_dict()
        self.sn_math = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
        if val in self.senior_electives:
            self.senior_electives.remove(val)
    def toggle_sn_math(self):
        self.sn_math_active = not self.sn_math_active

    

    #for physcs majors physics II and or Physics c e and m
    selected_senior_physics: set[str] = {"AP Physics C: Electricity & Magnetism"}
    # which C course the dropdown is on (mechanics or E&M)
    sn_phys_c: str = "AP Physics C: Electricity & Magnetism"

    def toggle_senior_physics(self, course_name: str):
        #makes sure physics majors keep atleast one
        if course_name in self.selected_senior_physics:
            if len(self.selected_senior_physics) > 1:
                self.selected_senior_physics.remove(course_name)
                if course_name == "AP Physics II":
                    self.change_sn_phys_c("AP Physics C: Electricity & Magnetism")
        else:
            self.selected_senior_physics.add(course_name)
            if self.senior_periods > 10 or self.senior_ap_count > 3:
                self.selected_senior_physics.remove(course_name)

    def change_sn_phys_c(self, new_course: str):
        # set has no index, so swap by remove + add (only if the old one was selected)
        if self.sn_phys_c in self.selected_senior_physics:
            self.selected_senior_physics.remove(self.sn_phys_c)
            self.selected_senior_physics.add(new_course)
        self.sn_phys_c = new_course

    def change_j_eng(self, val: str):
        snapshot = self._export_progress_dict()
        self.j_eng = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_sn_eng(self, val: str):
        snapshot = self._export_progress_dict()
        self.sn_eng = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_sn_his(self, val: str):
        snapshot = self._export_progress_dict()
        self.sn_his = val
        if val == "None (free period, econ junior year)":
            self.j_his = "Economics"
        if val == "None (free period, gov junior year)":
            self.j_his = "Participation in Government"
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_sn_ec(self, val: str):
        snapshot = self._export_progress_dict()
        self.sn_ec = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)
    def change_sn_gov(self, val: str):
        snapshot = self._export_progress_dict()
        self.sn_gov = val
        self._evict_duplicates()
        if not self._enforce_period_limits():
            self._import_progress_dict(snapshot)

    def _calculate_total_periods(self, year: str) -> int:
        return calculate_total_periods(self._courses_for_year(year))

    @rx.var
    def freshman_periods(self) -> int:
        return self._calculate_total_periods("Freshman")

    @rx.var
    def sophomore_periods(self) -> int:
        return self._calculate_total_periods("Sophomore")

    

    @rx.var
    def junior_periods(self) -> int:
        return self._calculate_total_periods("Junior")

    @rx.var
    def senior_periods(self) -> int:
        return self._calculate_total_periods("Senior")

    @rx.var
    def freshman_course_count(self) -> int:
        return len(self._courses_for_year("Freshman"))

    @rx.var
    def sophomore_course_count(self) -> int:
        return len(self._courses_for_year("Sophomore"))

    @rx.var
    def junior_course_count(self) -> int:
        return len(self._courses_for_year("Junior"))

    @rx.var
    def senior_course_count(self) -> int:
        return len(self._courses_for_year("Senior"))

    @rx.var
    def total_course_count(self) -> int:
        return (self.freshman_course_count + 
                self.sophomore_course_count + 
                self.junior_course_count + 
                self.senior_course_count)

    
    
    # --- AP Course Counters ---
    @rx.var
    def freshman_ap_count(self) -> int:
        count = 0
        for c in self._courses_for_year("Freshman"):
            # pre ap world is not ap
            if c[:2] == "AP":
                count += 1
        return count

    @rx.var
    def sophomore_ap_count(self) -> int:
        return sum(1 for c in self._courses_for_year("Sophomore") if "AP" in c)

    @rx.var
    def junior_ap_count(self) -> int:
        return sum(1 for c in self._courses_for_year("Junior") if "AP" in c)

    @rx.var
    def senior_ap_count(self) -> int:
        return sum(1 for c in self._courses_for_year("Senior") if "AP" in c)
    
  
    
    # --- Global Pop-up Event Actions ---
    def set_search_query(self, val: str):
        self.search_query = val

    def close_course_details(self):
        self.is_detail_open = False
    
    def open_course_details(self, name: str):
        data = COURSE_CATALOG.get(name, {})
        self.active_modal_course = {
            "name": name,
            "description": data.get("description", "No description available for this course yet."),
            "periods": str(data.get("periods", 1)),
            "credits": str(data.get("credits", 1.0)),
            "is_elective": data.get("is_elective", False),
            "semesters": str(data.get("semesters", 2)),
            "grade_badges": grade_badges(
                data.get("is_elective", False),
                data.get("grades", []),
                data.get("available_grades", [])
            ),
        }
        self.is_detail_open = True

    def open_search_for_grade(self, grade_name: str):
        self.current_modal_grade = grade_name
        self.search_query = ""

    def add_course(self, course_name: str, target_year: str):
        if target_year == "Freshman" and course_name not in self.freshman_electives:
            self.freshman_electives.append(course_name)
        elif target_year == "Sophomore" and course_name not in self.sophomore_electives:
            self.sophomore_electives.append(course_name)
        elif target_year == "Junior" and course_name not in self.junior_electives:
            self.junior_electives.append(course_name)
        elif target_year == "Senior" and course_name not in self.senior_electives:
            self.senior_electives.append(course_name)
        self._evict_duplicates()

    def delete_course(self, course_name: str, target_year: str):
        junior_reqs = MAJORS[self.major].get("Junior", [])
        senior_reqs = MAJORS[self.major].get("Senior", [])
        
        if course_name in junior_reqs or course_name in senior_reqs:
            return rx.window_alert(f"Cannot delete {course_name}! This course is a core requirement for {self.major}.")
            
        if target_year == "Freshman" and course_name in self.freshman_electives:
            self.freshman_electives.remove(course_name)
        elif target_year == "Sophomore" and course_name in self.sophomore_electives:
            self.sophomore_electives.remove(course_name)
        elif target_year == "Junior" and course_name in self.junior_electives:
            self.junior_electives.remove(course_name)
        elif target_year == "Senior" and course_name in self.senior_electives:
            self.senior_electives.remove(course_name)

    # --- Computed Vars ---
    @rx.var(cache=True)
    def room(self) -> str: return MAJORS[self.major].get("room", "N/A")

    @rx.var(cache=True)
    def major_note(self) -> str: return MAJORS[self.major].get("note", "")

    @rx.var(cache=True)
    def math_is_accelerated(self) -> bool: return self.pre_credits.get("Geometry", False)

    @rx.var
    def took_ap_calc_bc_junior(self) -> bool:
        return self.math_is_accelerated or self.j_math == "AP Calculus BC" or self.j_math == "AP Calculus AB"

    @rx.var(cache=True)
    def lang_is_accelerated(self) -> bool: return "II" in self.f_lang

    @rx.var(cache=True)
    def language_base(self) -> str: return self.f_lang.split()[0] if self.f_lang else ""

    @rx.var(cache=True)
    def took_seminar(self) -> bool: return self.so_eng == "AP Capstone Seminar"

    @rx.var(cache=True)
    def chose_economics_jr(self) -> bool: 
        took_reg_econ = self.j_his == "Economics"
        return took_reg_econ
    
    @rx.var(cache=True)
    def chose_african_jr(self) -> bool:
        return self.j_his == "AP African American Studies" 
    @rx.var(cache=True)
    def chose_government_jr(self) -> bool:
        return (
            ("AP US Government" in self.junior_major_courses or 
            "AP US Government" in self.junior_electives) or ("AP US Government" in self.senior_major_courses or "AP US Government" in self.senior_electives) or ("AP Comparative Government" in self.senior_electives or "AP Comparative Government" in self.junior_electives)
        )
    @rx.var(cache = True)
    def has_macro(self) -> bool:
        return ("AP Macroeconomics with Government" in self.junior_major_courses or "AP Macroeconomics with Government" in self.senior_major_courses)

#----------------------------------------Gov / econ stuff-------------------------------------------
    @rx.var(cache=True)
    def has_econ_gov_conflict(self) -> bool:
        #True if the student already has AP Macroeconomics or AP Macroeconomics / AP Microeconomics (One Semester each)
        conflict_courses = {
            "AP Macroeconomics with Government",
            "AP Macroeconomics / AP Microeconomics",
        }
        sources = (
            self.junior_major_courses + self.senior_major_courses +
            self.junior_electives + self.senior_electives
        )
        return any(c in conflict_courses for c in sources)
    @rx.var(cache=True)
    def has_gov_conflict(self) -> bool:
        #if student is LAS major or taking ap us gov
        return self.major == "Law & Society" or "AP US Government" in MAJORS[self.major].get("Junior", [])
    @rx.var(cache=True)
    def chose_gov_jr_finance(self) -> bool:
        return self.major == "Finance" and self.j_his == "Participation in Government"

    @rx.var(cache=True)
    def needs_sn_ec(self) -> bool:
        # senior year economics dropdown only shows up when a gov course is the senior history pick
        if self.has_macro or self.chose_economics_jr or self.chose_government_jr:
            return False
        if self.has_econ_gov_conflict:
            return False
        return self.sn_his in SENIOR_GOV_COURSES

#-------------------------------------------------------------------------------------------------
    @rx.var(cache=True)
    def has_ap_physics_junior(self) -> bool: return any("AP Physics I" in c for c in MAJORS[self.major].get("Junior", []))

    @rx.var(cache=True)
    def need_regents_physics_junior(self) -> bool: 
        if "AP Physics I" in self.junior_electives or "AP Physics I" in self.senior_electives:
            return False
        return (self.f_sci != "Regents Physics") and not self.has_ap_physics_junior

    @rx.var(cache=True)
    def junior_ap_room_for_physics(self) -> bool:
        """Whether there's room for another AP junior year, not counting the
        Regents Physics / AP Physics I swap slot itself."""
        others = [c for c in self._courses_for_year("Junior") if "AP" in c and c != self.j_phys]
        return len(others) < 3
    

    @rx.var(cache=True)
    def junior_major_courses(self) -> list[str]:
        courses = MAJORS[self.major].get("Junior", [])
        final_courses = []
        for c in courses:
            if "AP Biology" in c and self.f_sci == "AP Biology":
                final_courses.append("AP Chemistry")
            else:
                final_courses.append(c)
        return final_courses

    @rx.var(cache=True)
    def senior_major_courses(self) -> list[str]:
        courses = MAJORS[self.major].get("Senior", [])

        if self.major == "LIU Pharmacy" and self.f_sci == "AP Biology":
            courses = [course for course in courses if course != "AP Biology"]

        return courses
    # --- Math Major Overrides and Filtering Backend ---
    @property
    def _math_overrides(self) -> list[str]:
        return ["AP Calculus AB", "AP Calculus BC", "Multivariable Calculus", "Pre-Calculus"]

    @rx.var
    def junior_math_override(self) -> str:
        if self.major == "Applied Mathematics" or self.major == "LIU Pharmacy":
            return "Mathematics Major Override"
        for c in self.junior_major_courses:
            if any(kw in c for kw in self._math_overrides):
                return c
        return ""

    @rx.var
    def senior_math_override(self) -> str:
        if self.major == "Applied Mathematics" or self.major == "LIU Pharmacy":
            return "Mathematics Major Override"
        for c in self.senior_major_courses:
            if any(kw in c for kw in self._math_overrides):
                return c
        return ""

    @rx.var
    def filtered_junior_major_courses(self) -> list[str]:
        return [c for c in self.junior_major_courses if c not in self._math_overrides]

    @rx.var
    def filtered_senior_major_courses(self) -> list[str]:
        return [c for c in self.senior_major_courses if c not in self._math_overrides]

    
    def _courses_for_year(self, year: str) -> set:
        if year == "Freshman":
            return set([
                "Design & Drafting for Production (DDP)", "English 9",
                self.f_hist, self.f_sci, self.f_lang, "Physical Education", "Lunch" 
            ] + self.freshman_math_courses + self.freshman_electives)

        if year == "Sophomore":
            math = "Pre-Calculus" if self.math_is_accelerated else "Algebra II"
            lang = (self.language_base + " III") if self.lang_is_accelerated else (self.language_base + " II")
            courses = ([
                "AP Computer Science Principles", "Health Education", self.so_eng, self.so_hist,
                "Regents Chemistry", math, lang, "Physical Education", "Lunch" 
            ] + self.sophomore_electives)
            
            return set(courses)
            
        if year == "Junior":
            math = self.j_math
            # Start with dropdowns and electives as a clean list
            courses = [ self.j_his, "Physical Education", "Lunch"] + self.junior_electives

            if self.major != "LIU Pharmacy":
                courses.append(self.j_eng)

            # 🎯 If they chose Economics in Junior year, dynamically inject Government into Junior year active tracker
            if (self.j_his == "Economics" or (
                "AP Macroeconomics / AP Microeconomics (One Semester each)" in self.junior_major_courses or 
                "AP Macroeconomics / AP Microeconomics (One Semester each)" in self.junior_electives
            )) and not self.has_econ_gov_conflict and not self.chose_government_jr and not self.has_gov_conflict:
                courses.append(self.sn_gov)
            
            if self.junior_math_override != "":
                courses.extend(self.filtered_junior_major_courses)
                courses.append(math)
            else:
                courses.extend(self.junior_major_courses)
                courses.append(math)
                
            if not self.lang_is_accelerated:
                courses.append(self.language_base + " III")
            if self.need_regents_physics_junior:
                courses.append(self.j_phys)
            return set(c for c in courses if c not in self.none_history_placeholders)
        
        if year == "Senior":

            math = self.sn_math if self.sn_math else "AP Calculus BC"
            courses = [self.sn_eng, "Physical Education", "Lunch"] + self.senior_electives
            
            if self.major == "Physics":
                if math and self.sn_math_active:
                    courses.append(math)
                courses.extend(list(self.selected_senior_physics))
                courses.append("Modern Physics") 
            else:
                if self.senior_math_override != "":
                    courses.extend(self.filtered_senior_major_courses)
                else:
                    courses.extend(self.senior_major_courses)
                if math and self.sn_math_active:
                    courses.append(math)
            # only track senior history rules if they didn't choose economics in junior year
            if self.has_macro:
                pass
            elif not self.chose_economics_jr:
                if self.chose_government_jr:
                    courses.append("Economics")
                else:
                    courses.append(self.sn_his)
                    if self.needs_sn_ec:
                        courses.append(self.sn_ec)
                    if self.sn_his == "Economics" and not self.has_gov_conflict:
                        courses.append(self.sn_gov)


            return set(c for c in courses if c not in self.none_history_placeholders)
    @rx.var
    def all_courses(self) -> set[str]:
        return self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior") | self._courses_for_year("Senior") 
    
    def _evict_duplicates(self):
        fr = self._courses_for_year("Freshman")
        so = self._courses_for_year("Sophomore")
        jr = self._courses_for_year("Junior")

        prior_after_fr = fr
        prior_after_so = fr | so
        prior_after_jr = fr | so | jr

        if self.so_eng in prior_after_fr and self.so_eng != "English 10":
            self.so_eng = "English 10"
        if self.so_hist in prior_after_fr:
            self.so_hist = "Regents Global History"
        self.sophomore_electives = [c for c in self.sophomore_electives if c not in prior_after_fr or COURSE_CATALOG.get(c, {}).get("allow_multiple", False)]

        if self.j_eng in prior_after_so:
            self.j_eng = "English 11"
        if self.j_his in prior_after_so:
            self.j_his = "Regents US History"
        if self.j_his == "Economics" and self.has_econ_gov_conflict:
            self.j_his = "Regents US History"
            self.sn_his = "Economics"
        self.junior_electives = [c for c in self.junior_electives if c not in prior_after_so or COURSE_CATALOG.get(c, {}).get("allow_multiple", False)]

        if self.sn_eng in prior_after_jr:
            self.sn_eng = "Creative Writing"
        if self.sn_his in prior_after_jr:
            self.sn_his = "Participation in Government"
        if self.sn_ec in prior_after_jr:
            self.sn_his = "Participation in Government"
        if self.sn_gov in prior_after_jr:
            self.sn_gov = "Participation in Government"
        self.senior_electives = [c for c in self.senior_electives if c not in prior_after_jr or COURSE_CATALOG.get(c, {}).get("allow_multiple", False)]

    def _enforce_ap_limits(self):
        if self.junior_ap_count > 3:
            if "AP" in self.j_eng: self.j_eng = "English 11"
            if "AP" in self.j_his: self.j_his = "Regents US History"
            if "AP" in self.j_phys: self.j_phys = "Regents Physics"
            if "AP" in self.j_math and not self.math_is_accelerated: self.j_math = "Pre-Calculus"
            while self.junior_ap_count > 3:
                ap_els = [c for c in self.junior_electives if "AP" in c]
                if not ap_els: break
                self.junior_electives.remove(ap_els[0])
        if self.senior_ap_count > 3:
            if "AP" in self.sn_eng: self.sn_eng = "Creative Writing"
            if "AP" in self.sn_his: self.sn_his = "Economics"
            if "AP" in self.sn_ec: self.sn_ec = "Economics"
            while self.senior_ap_count > 3:
                ap_els = [c for c in self.senior_electives if "AP" in c]
                if not ap_els: break
                self.senior_electives.remove(ap_els[0])

    def _enforce_period_limits(self) -> bool:
        
        year_to_electives = {
            "Freshman": "freshman_electives",
            "Sophomore": "sophomore_electives",
            "Junior": "junior_electives",
            "Senior": "senior_electives",
        }
        ok = True
        for year, attr in year_to_electives.items():
            while self._calculate_total_periods(year) > 10:
                electives = getattr(self, attr)
                if not electives:
                    ok = False
                    break  # over the cap with no electives left to cut — nothing more to auto-fix
                electives.pop(0) 
        return ok

    
    def compute_filtered_catalog(self) -> list[dict]:
        grade = str(self.current_modal_grade).strip()
        years = ["Freshman", "Sophomore", "Junior", "Senior"]
        periods = {
            "Freshman": self.freshman_periods, "Sophomore": self.sophomore_periods,
            "Junior": self.junior_periods, "Senior": self.senior_periods,
        }
        ap_counts = {
            "Freshman": self.freshman_ap_count, "Sophomore": self.sophomore_ap_count,
            "Junior": self.junior_ap_count, "Senior": self.senior_ap_count,
        }
        # an unrecognized grade is treated as senior
        year = grade if grade in years else "Senior"
        return search_electives(
            query=self.search_query,
            grade=grade,
            major=self.major,
            language_base=self.language_base,
            lang_is_accelerated=self.lang_is_accelerated,
            chose_economics_jr=self.chose_economics_jr,
            took_ap_calc_bc_junior=self.took_ap_calc_bc_junior,
            courses_by_year={y: self._courses_for_year(y) for y in years},
            current_periods=periods[year],
            ap_count=ap_counts[year],
        )
   #login 

    @rx.var
    def filtered_catalog(self) -> list[dict]:
        return self.compute_filtered_catalog()
    
    @rx.var
    def filtered_catalog_count(self) -> int:
        return len(self.filtered_catalog)
    @rx.var
    def dropdown_colors(self) -> dict[str, str]:
        return {name: data.get("color", "#1e2025") for name, data in COURSE_CATALOG.items()}
