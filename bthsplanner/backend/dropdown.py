import re

import reflex as rx

from data.courses import req_courses

from .state import PlannerState


def _expand_taken(taken: set) -> set:
    expanded = set()
    for t in taken:
        expanded.add(t)
        if " / " in t:
            for part in t.split(" / "):
                clean = part.strip()
                expanded.add(clean)
                no_paren = re.sub(r'\s*\(.*?\)\s*$', '', clean).strip()
                if no_paren != clean:
                    expanded.add(no_paren)
    return expanded


def _filter(opts: list, current: str, ap_count: int, taken: set) -> list:
    expanded = _expand_taken(taken)
    other_ap_count = ap_count - (1 if "AP" in current else 0)
    at_limit = other_ap_count >= 3
    return [
        o for o in opts
        if (o == current or o not in expanded)
        and (o == current or "AP" not in o or not at_limit)
    ]
class DropdownOptions(PlannerState):
    
    @rx.var
    def f_sci_opts(self) -> list[str]:
        has_bio = self.pre_credits.get("Biology/Living Environment", False)
        
        if not has_bio:
            opts = ["Regents Biology"]
        else:
            opts = ["Regents Physics", "AP Biology"]
        return _filter(opts, self.f_sci, self.freshman_ap_count , set())

    @rx.var
    def so_eng_opts(self) -> list[str]:
        opts = ["English 10", "AP Capstone Seminar"]
        return _filter(opts, self.so_eng, self.sophomore_ap_count , self._courses_for_year("Freshman"))
    
    @rx.var
    def so_hist_opts(self) -> list[str]:
        opts = ["AP European History", "AP World History", "Regents Global History"]
        return _filter(opts, self.so_hist, self.sophomore_ap_count , self._courses_for_year("Freshman"))
    
    @rx.var
    def j_eng_opts(self) -> list[str]:
        opts = ["AP English Language & Composition", "English 11"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore")
        return _filter(opts, self.j_eng, self.junior_ap_count , prior)
    
    @rx.var
    def j_his_opts(self) -> list[str]:
        if self.has_econ_gov_conflict: #finance majors have econ gov conflict, macro/micro leaves gov to be taken later or in the same year
            opts = ["AP US History", "Regents US History", "Participation in Government", "AP African American Studies", "None (free period, gov senior year)"]
        else:
            opts = ["AP US History", "Regents US History", "Economics", "AP African American Studies", "None (free period, econ senior year)"]
        if self.has_econ_gov_conflict:
            opts = [o for o in opts if o not in ("Economics",)]

        if not self.pre_credits.get("US History", False):
            if self.major != "Finance":
                opts = [o for o in opts if o not in ("Participation in Government", "Economics", "None (free period, econ senior year)")]
            else:
                opts = [o for o in opts if o not in ("Participation in Government", "Economics", "None (free period, gov senior year)")]
        else: opts = [o for o in opts if o not in ("Regents US History")]
        
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore")
        return _filter(opts, self.j_his, self.junior_ap_count ,prior)
    
    @rx.var
    def j_math_opts(self) -> list[str]:
        opts = ["AP Calculus AB", "AP Calculus BC"] if self.math_is_accelerated else ["Pre-Calculus", "AP Calculus AB", "AP Calculus BC"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore")
        return _filter(opts, self.j_math, self.junior_ap_count, prior)
    
    @rx.var
    def j_phys_opts(self) -> list[str]:
        return ["Regents Physics", "AP Physics I"]
    
    @rx.var
    def sn_calcs(self) -> list[str]:
        return ["AP Calculus BC", "AP Calculus AB"]
    
    @rx.var
    def sn_math_opts(self) -> list[str]:
        if self.major == "LIU Pharmacy":
            opts = ["Multivariable Calculus", "Linear Algebra", "AP Calculus BC"] if self.j_math == "AP Calculus AB" else ["Multivariable Calculus", "Linear Algebra"]
        elif self.senior_math_override:
            opts = ["Multivariable Calculus", "AP Calculus BC"] if self.j_math == "AP Calculus AB" else ["Multivariable Calculus"]    
        else:
            opts = ["Multivariable Calculus", "Linear Algebra", "AP Calculus BC"] if self.j_math == "AP Calculus AB" else ["Multivariable Calculus", "Linear Algebra"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior")
        return _filter(opts, self.sn_math, False, prior)
    
    @rx.var
    def sn_eng_opts(self) -> list[str]:
        opts = ["AP Capstone Research", "AP English Literature & Composition", "Creative Writing", "Film & Literature", "Graphic Novels", "Journalism", "Science Fiction & Fantasy", "Mystery, Horror & the Supernatural", "Live, Love, & Death", "Drama", "Yearbook"] if self.so_eng == "AP Capstone Seminar" else [ "AP English Literature & Composition", "Creative Writing", "Film & Literature", "Graphic Novels", "Journalism", "Science Fiction & Fantasy", "Mystery, Horror & the Supernatural", "Live, Love, & Death", "Drama", "Yearbook"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior")
        return _filter(opts, self.sn_eng, self.senior_ap_count , prior)
    
    @rx.var
    def sn_his_opts(self) -> list[str]:
        if self.has_econ_gov_conflict:
            opts = ["AP US Government", "Participation in Government", "AP Comparative Government"]
            if self.pre_credits.get("US History", False):
                opts.append("None (free period, gov junior year)")
        else:
            opts = ["AP Macroeconomics with Government", "Economics", "AP US Government", "Participation in Government", "AP Comparative Government"]
            if self.pre_credits.get("US History", False):
                opts.append("None (free period, econ junior year)")
            
            if self.major == "Law & Society":
                opts.remove("AP US Government")
        if self.chose_government_jr:
            opts = [o for o in opts if o not in ("Participation in Government", "AP Comparative Government")]

        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior")
        return _filter(opts, self.sn_his, self.senior_ap_count, prior)
      
    @rx.var
    def sn_ec_opts(self) -> list[str]:
        opts = [#"AP Macroeconomics with Government", 
                "Economics"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior")
        return _filter(opts, self.sn_ec, self.senior_ap_count , prior)
    
    @rx.var
    def sn_gov_opts(self) -> list[str]:
        opts = ["AP US Government", "Participation in Government", "AP Comparative Government"]
        prior = self._courses_for_year("Freshman") | self._courses_for_year("Sophomore") | self._courses_for_year("Junior")
        return _filter(opts, self.sn_gov, self.senior_ap_count, prior)
    
    @rx.var
    def sn_phys_c_opts(self) -> list[str]:
        return ["AP Physics C: Mechanics", "AP Physics C: Electricity & Magnetism"]


MAJOR_COURSE_COLOR = req_courses