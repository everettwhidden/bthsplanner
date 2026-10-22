english_color = "var(--english_color)"
history_color =  "var(--history_color)"
science_color = "var(--science_color)"
math_color = "var(--math_color)"
lang_color = "var(--lang_color)"
req_courses = "var(--req_courses)"
elective_color = "var(--elective_color)"
gym_lunch_color = "var(--gym_lunch_color)"



COURSE_CATALOG = {
    "AP African American Studies": {
            "description": "AP African American Studies is an interdisciplinary high school course exploring the history, culture, and vital contributions of African Americans. Spanning from early African kingdoms to modern times, the curriculum blends history, literature, the arts, science, and political science.",
            "periods": 1,
            "credits": 1.0,
            "is_elective": False,
            "grades" : ["Junior"],
            "color" : history_color
        },
    "AP Biology": {
        "description": "This college-level, double-period course explores biology through four big ideas: evolution, energy and matter processing, information storage and transmission, and biological systems interactions. The curriculum is lab-intensive, with students designing experiments and analyzing data on topics ranging from molecular genetics to ecology.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "grades" : ["Freshman", "Junior", "Senior"],
        "color" : science_color
    },
    "AP Business with Personal Finance": {
        "description": "This course introduces students to core business principles and personal financial literacy, covering topics such as entrepreneurship, marketing, economics, budgeting, credit, investing, and financial planning. It prepares students for the AP exam while building practical skills for managing personal finances.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"],
    },
    "AP Calculus AB": {
        "description": "This college-level course covers differential and integral calculus of a single variable, including limits, derivatives and their applications, and an introduction to definite and indefinite integrals. It corresponds to a first-semester college calculus course and prepares students for the AP Calculus AB exam.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior", "Senior"],
        "color" : math_color
    },
    "AP Calculus BC": {
        "description": "This fast-paced, double-period course covers everything in AB Calculus plus additional integration techniques, sequences and series (including Taylor and Maclaurin series), and polar, parametric, and vector-valued functions. It corresponds to a full year of college calculus and is the accelerated math track for students moving on to Multivariable Calculus or Linear Algebra senior year.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior", "Senior"],
        "color" : math_color
    },
    
    
    "AP Chemistry": {
        "description": "This rigorous, double-period, college-level chemistry course covers atomic structure, chemical bonding, kinetics, thermodynamics, equilibrium, and acid-base and electrochemistry, with an emphasis on quantitative reasoning and lab-based evidence. Students complete guided-inquiry labs that mirror introductory college chemistry coursework.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"],
        
    },
    "AP Chinese Language & Culture": {
        "description": "A rigorous, college-level immersion course designed to hone interpersonal, interpretive, and presentational communication skills in Mandarin. Students engage with authentic audio, visual, and written materials to explore contemporary societal issues, global challenges, and deep-rooted cultural values.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"],
        
    },
    "AP Comparative Government": {
        "description": "AP Comparative Government and Politics introduces students to the rich diversity of political life outside the United States. The course uses a comparative approach to examine the political structures; policies; and political, economic, and social challenges of six selected countries: China, Iran, Mexico, Nigeria, Russia, and the United Kingdom. Students compare the effectiveness of approaches to many global issues by examining how different governments solve similar problems. They will also engage in disciplinary practices that require them to read and interpret data, make comparisons and applications, and develop evidence-based arguments.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": [ "Senior"],
        "semesters" : 1,
        "color" : history_color
    },
    "AP Computer Science Applications - JAVA": {
        "description": "This is the core junior-year course for the Software Engineering major, teaching object-oriented programming in Java, including classes, arrays, and 2D array structures, alongside algorithm design and analysis. Students build a portfolio of Java programs while preparing for the AP Computer Science A exam.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior"]
    },
    "AP Computer Science Principles": {
        "description": "This required underclassman course introduces the big ideas of computer science, including creative development, data and information, algorithms, computing systems, and the internet, alongside the social and ethical implications of computing. Using a block-based/visual language such as Snap!, students build programs, work with data, and complete a create performance task, laying the groundwork for later programming coursework and the AP CSP exam.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Sophomore"],
        "color" : req_courses
    },
    "AP Cybersecurity": {
        "description": "This course provides an in-depth introduction to the principles and practices of modern cybersecurity. Students explore the fundamentals of computer networks, operating systems, and how these systems can be exploited or defended, covering topics such as cryptography, authentication, malware analysis, network defense, penetration testing, and digital forensics. The curriculum also addresses risk assessment and management, security policy design, and incident response protocols, while examining the legal, ethical, and societal implications of cybersecurity, including privacy law and responsible disclosure. Through hands-on labs and case studies, students develop practical skills in identifying system vulnerabilities, implementing security controls, and thinking critically about how to protect data and infrastructure in an increasingly connected world.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"],
    },
    "AP English Language & Composition": {
        "description": "This college-level course focuses on rhetorical analysis and argumentative writing, primarily through nonfiction texts, speeches, and essays. Students practice synthesizing multiple sources, analyzing an author's rhetorical choices, and constructing their own persuasive, evidence-based essays under timed conditions in preparation for the AP exam.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Junior"],
        "color": english_color
    },
    "AP English Literature & Composition": {
        "description": "This college-level course emphasizes close literary analysis of poetry, drama, and prose spanning multiple centuries and traditions. Students write frequent analytical and argumentative essays examining how literary elements like structure, symbolism, and character shape meaning, preparing them for the AP exam and college-level literary study.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Senior"],
        "color": english_color
    },
    "AP Environmental Science": {
        "description": "This college-level, double-period course examines the interrelationships within the natural world, covering ecosystems, biodiversity, natural resources, pollution, and the environmental and societal impact of human activity. The course includes fieldwork and lab investigations, such as water, soil, and air testing.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"]
    },
    "AP European History": {
        "description": "This college-level course surveys European political, economic, social, and intellectual history from roughly 1450 to the present, examining developments such as the Renaissance, Reformation, Enlightenment, industrialization, and the World Wars. Students practice document-based and long-essay historical argumentation in preparation for the AP exam.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Sophomore"],
        "color" : history_color
    },
    "AP French Language & Culture": {
        "description": "A college-level course conducted entirely in French that deepens linguistic accuracy and cultural synthesis across six thematic areas. Students interpret authentic French literature, news broadcasts, and podcasts to construct persuasive essays and spoken presentations.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP German Language & Culture": {
        "description": "An advanced college-level course focusing on real-world application of the German language through global, environmental, and historical themes. Students refine their analytical reading and listening skills using authentic German media to produce high-level written essays and oral arguments.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP Human Geography": {
        "description": "This college-level course examines patterns and processes in human settlement, migration, culture, political organization, agriculture, and economic development across the globe. Students learn to interpret and apply spatial concepts and models to real-world geographic phenomena.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Junior", "Senior"],
        "color" : history_color
    },
    "AP Italian Language & Culture": {
        "description": "A college-level, theme-based immersion course designed to maximize spoken and written accuracy in Italian. Students evaluate authentic materials, such as articles, interviews, and literature, to engage in complex cultural comparisons and formal argumentative expressions.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP Macroeconomics / AP Microeconomics": {
        "description": "This junior-year Finance major sequence splits the year between the two College Board AP economics courses: AP Macroeconomics for one semester, covering national income, unemployment, inflation, the aggregate supply and demand model, and fiscal and monetary policy, and AP Microeconomics for the other semester, covering supply and demand, consumer and producer theory, market structures, factor markets, and market failure. Together they give Finance majors college-level grounding in both branches of economics before senior year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"],
        
    },
    "AP Macroeconomics with Government": {
        "description": "This year-long senior course pairs AP Macroeconomics in the first semester, covering national income, unemployment and inflation, aggregate supply and demand, and fiscal and monetary policy, with a second semester of Participation in Government, covering civic structures, public policy, and the workings of local, state, and federal institutions.",
        "periods": 1,
        "credits": 2.0,
        "is_elective": True,
        "available_grades" : ["Senior"],
        "color" : history_color
    },
    "AP Physics C: Electricity & Magnetism": {
        "description": "This calculus-based, double-period senior course covers the AP Physics C: Mechanics curriculum during the first semester and the AP Physics C: Electricity & Magnetism curriculum during the second semester. The E&M curriculum covers electrostatics, conductors and capacitors, dielectrics, DC and RC circuits, magnetic fields, and electromagnetic induction. This course corresponds to a first and second-semester calculus-based college physics course. This course is viewed as the gold standard for students looking to go into engineering. Seats are limited, with physics majors getting automatic priority seating and very few non-physics major spots available.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "available_grades" : ["Senior"]
    },
    "AP Physics C: Mechanics": {
        "description": "This calculus-based senior-year physics course, popular among engineering-track majors, covers kinematics, Newton's laws, work and energy, linear and angular momentum, rotational motion, and oscillations using derivatives and integrals. It corresponds to an introductory calculus-based college mechanics course.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "available_grades" : ["Senior"]
    },
    "AP Physics I": {
        "description": "This algebra-based, double-period, college-level course covers Newtonian mechanics in depth, including kinematics, dynamics, circular motion and gravitation, energy, momentum, simple harmonic motion, torque and rotational motion, and an introduction to fluid mechanics. The course is inquiry-based, with students designing and running their own lab investigations to build and test physical models.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior"],
        "color" : science_color
    },
    "AP Physics II": {
        "description": "This advanced, algebra-based, double-period senior course explores classical and modern physics through complex, macro-level systems. Moving beyond basic mechanics, students study fluid dynamics and thermodynamics to analyze fluid pressure, ideal gases, and heat engine efficiency. The curriculum covers electromagnetism, including electric fields, capacitance, dynamic DC circuits, and electromagnetic induction, before shifting to geometric and physical optics to model the behavior, reflection, and interference of light, and concludes with an introduction to quantum, atomic, and nuclear physics, including the photoelectric effect, nuclear decay, and mass-energy equivalence, all supported by rigorous laboratory inquiry.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": True,
        "available_grades" : ["Senior"]
    },
    "AP Psychology": {
        "description": "This college-level course surveys the scientific study of behavior and mental processes, covering topics such as biological bases of behavior, learning, cognition, developmental psychology, personality, and psychological disorders. Students learn to evaluate psychological research methods and apply psychological concepts to real-world behavior.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "available_grades" : ["Senior"]
    },
    "AP Capstone Research": {
        "description": "AP Research is an advanced, college-level inquiry course that cultivates the skills necessary for rigorous, independent scholarship. Building upon the foundational competencies developed in AP Seminar, students design, plan, and execute a year-long, evidence-based investigation into a self-selected topic of academic or real-world significance. The curriculum emphasizes the mastery of research methodologies, ethical research practices, and the synthesis of new knowledge. The course culminates in a comprehensive, 4,000-to-5,000-word academic thesis paper and a formal presentation with an oral defense before an institutional panel.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Senior"],
        "color": english_color
    },
    "AP Capstone Seminar": {
        "description": "The foundational course of the College Board's AP Capstone program, AP Seminar teaches students to investigate real-world issues from multiple perspectives, evaluate the credibility and bias of varied sources, and build their own evidence-based arguments. Students complete a team project and presentation as well as an individual research-based essay and presentation, both assessed by the College Board.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Sophomore"],
        "color": english_color
    },
    "AP Spanish Language & Culture": {
        "description": "A rigorous, college-level immersion class designed to polish integrated language skills across real-world themes. Students synthesize authentic print and audio resources to participate in sophisticated debates, write formal reports, and deliver analytical oral presentations.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP Statistics": {
        "description": "This college-level course introduces the four major themes of statistics: exploring data, sampling and experimental design, probability, and statistical inference. Students design studies, analyze real data sets, and learn to draw and justify conclusions using confidence intervals and hypothesis tests.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP Studio Art 2D": {
        "description": "Students will create and evaluate works in all 3 aspects of the portfolio (quality, concentration, and breadth). Everyone will be required to submit portfolios for evaluation at the College Board set dates. During the development of this portfolio students will work both in and out of the classroom to experience a variety of concepts and techniques in creative problem solving. Students will also create a section of work that is of personal interest. Everyone will be encouraged to create solutions that are “outside the box” and will force both the innovator and the audience to see in a new way. We will explore many 2D materials including Photography, pencil, charcoal, design markers, collage mixed media as well as extensive drawing techniques.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "AP US Government": {
        "description": "This college-level course examines the foundations of the U.S. government, including the Constitution, federalism, the three branches, civil rights and liberties, and political behavior such as parties, elections, and public opinion. Students analyze foundational documents and Supreme Court cases and practice argumentative writing in preparation for the AP exam.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "available_grades" : ["Senior"],
        "color" : history_color,

    },
    "AP US History": {
        "description": "This college-level course surveys U.S. history from pre-Columbian societies through the present, covering major political, social, economic, and cultural developments. Students build skills in historical thinking, primary-source analysis, and essay writing aligned to the College Board's APUSH framework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Junior"],
        "color" : history_color
    },
    "AP World History": {
        "description": "AP World History: Modern is a college-level course that examines the global processes, connections, and conflicts that shaped humanity from 1200 CE to the present. Students analyze historical evidence, discern patterns of change and continuity, and construct evidence-based arguments across diverse societies and eras. The curriculum moves beyond mere memorization. It emphasizes the development of critical thinking skills, such as analyzing primary sources, assessing context, and evaluating historical causation.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 2,
        "is_elective": False,
        "available_grades" : ["Sophomore"],
        "color" : history_color
    },
    "Adobe Visual Design & Film Production": {
        "description": "This senior-year Media Communications major course covers film production using Adobe's video software, including narrative structure, multi-camera shooting techniques, and sound editing.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Senior"]
    },
    "Adobe Visual Design & Print Production": {
        "description": "This course builds skills in desktop publishing and print design using Adobe software, covering layout, typography, and preparing files for professional printing. It's taken by both Industrial Design and Media Communications majors as part of their senior-year Adobe coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Junior"]
    },
    "Advanced Modeling": {
        "description": "This senior-year Industrial Design major course extends CAD modeling skills to more advanced parametric design and complex surface geometry, building on the fundamentals learned junior year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Senior"]
    },
    "Advanced Spanish": {
        "description": "Bridges intermediate language acquisition and advanced literary analysis. Students refine stylistic writing and conversational nuance by exploring historical eras, cinematic works, and short stories from Latin America and Spain.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior","Senior"]
    },
    "Algebra II": {
        "description": "This course extends algebraic thinking to polynomial, rational, exponential, and logarithmic functions, along with an introduction to trigonometry and complex numbers. It builds the functional-thinking foundation required for Pre-Calculus and the AP Calculus sequence.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore"],
        "color" : math_color
    },
    "Algebra I": {
        "description": "This course covers foundational algebraic concepts including linear equations and inequalities, systems of equations, exponents, polynomials, and an introduction to functions. It builds the symbolic reasoning skills required for Geometry and the rest of the math sequence.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color": math_color
    },
    "American Concrete Institute Certification": {
        "description": "This senior-year Civil Engineering major course prepares students for an American Concrete Institute (ACI) field testing certification, covering the properties of fresh and hardened concrete, mix design, and standardized testing procedures used in the school's materials testing lab.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades" : ["Senior"]
    },
    "Analog Electronics": {
        "description": "This senior-year Electrical Engineering major course covers analog circuit analysis, including operational amplifiers, resistor-based circuits, and waveform generation and shaping, complementing the digital-circuit focus of the major's other electronics courses.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Senior"]
    },
    "Architectural Design & Modeling": {
        "description": "This senior-year Architecture major design studio has students develop detailed architectural projects from concept through construction-level documentation, including structural framing plans and scale physical or digital models. It's the capstone design course of the Architecture major, drawing on drafting, materials, and design skills built in earlier major courses.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Architectural Drawing with AutoCAD": {
        "description": "This junior-year Architecture major course develops technical drafting skills, including plan and section views, structural framing details, and building-code-compliant drawings, using industry-standard AutoCAD software. It builds the manual and digital drafting foundation used throughout the Architecture major's design studio courses.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Astronomy & Astrophysics": {
        "description": "This junior-year Physics major course covers the structure and behavior of celestial objects and systems, from stars and planets to galaxies and cosmology, introducing the physics used to study and model the universe.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior"]
    },
    "AutoCAD Certification": {
        "description": "This senior-year Civil Engineering major course prepares students for an industry-recognized AutoCAD certification exam, building proficiency in technical drafting and 2D/3D drawing used throughout civil design and construction documentation.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Band": {
        "description": "This pass/fail performing ensemble class develops instrumental technique and musicianship through the rehearsal and performance of a symphonic band repertoire. It's open to students in any grade and can be taken more than once.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Freshman", "Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Biochemistry/Chem E": {
        "description": "This senior-year, one-semester Chemistry major elective runs as one of two tracks depending on the section. The Chem E track, Introduction to Chemical Engineering, is an introductory course investigating stoichiometry with an emphasis on material and energy balances, covering types of chemical engineering processes, measuring pressure drops, processes involving chemical reactions, energy balances, and compressible gases, with a lab component run through case studies and simulations; the Biochemistry track instead applies chemistry to biological systems at the molecular level, such as enzyme function and metabolic reactions.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Bioorganic Chemistry": {
        "description": "This senior-year Neuroscience major course applies organic chemistry concepts to biological systems, covering topics such as enzyme active sites and the molecular mechanisms behind physiological processes relevant to neuroscience.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Building Materials & Fabrication": {
        "description": "This senior-year Architecture major course examines the physical properties, testing, and real-world performance of common building materials, alongside hands-on fabrication techniques and construction methods. Students analyze how material choices affect structural performance, cost, and design outcomes.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },

    "Chinese I": {
        "description": "An introduction to Mandarin Chinese focusing on modern Pinyin Romanization, basic character writing, and essential everyday vocabulary. Students build foundational speaking, listening, reading, and writing skills to navigate simple everyday conversations and explore core aspects of Chinese culture.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Junior", "Senior"],
        "color" : lang_color
    },
    "Chinese II": {
        "description": "Students expand their vocabulary and sentence structures to communicate more fluidly about personal routines, hobbies, and shopping. This course emphasizes paragraph-level reading comprehension, typing in Chinese characters, and deeper cultural engagement.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Sophomore"],
        "color" : lang_color
    },
    "Chinese III": {
        "description": "Prepares students for regional exams by strengthening complex grammar structures, formal vocabulary, and conversational spontaneity. Students analyze short literary texts and discuss social traditions, community dynamics, and historical trends.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore", "Junior"],
        "color" : lang_color
    },
    "Chorus": {
        "description": "This performing ensemble class develops vocal technique, sight-reading, and part-singing through the rehearsal and performance of choral repertoire. It's open to students in any grade and can be taken more than once.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Freshman", "Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Civil Law / Criminal Procedure": {
        "description": "This senior-year Law & Society major course covers courtroom procedure, evidence rules, jury processes, and civil tort actions, continuing the courtroom-simulation approach used throughout the major.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "AP US Government/Constitutional Law": {
        "description": "This junior-year Law & Society major course spends one semester on both AP US Government and Constitutional Law. Constitutional Law introduces constitutional law, covering foundational constitutional principles, landmark Supreme Court cases, and civil rights and liberties.",
        "periods": 1,
        "credits": 2.0,
        "semesters" : 2,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Constitutional Law II / Legal Research": {
        "description": "This senior-year Law & Society major course builds on Constitutional Law I with a deeper look at civil rights statutes and case law, alongside training in legal research and writing standard legal briefs.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Criminal Law": {
        "description": "This junior-year Law & Society major course, taught in Tech's dedicated courtroom space, covers the fundamentals of criminal statutes, offenses, and defenses. Students participate in simulations such as mock trials to apply legal concepts in practice.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Cultural & Physical Anthropology": {
        "description": "This senior-year Social Science Research major course covers both cultural anthropology, the comparative study of human societies and traditions, and physical anthropology, including human skeletal and evolutionary development.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Creative Writing": {
        "description": "The overall goal of this course is to play and to experiment with language and storytelling across multiple genres such as short fiction, poetry, drama, screenplays, graphic novels, and even illustrated books for children. We’ll learn by reading, by analyzing, and by emulating a diversity of successful writers in these genres, both classic and contemporary. We’ll learn what it takes to be artists, both spontaneous and disciplined, toward something worth saying –who we are at the core, who we’ve become, and how we each view the world through our own personal experiences and cultural orientations. Whether in small-group workshops or in whole-class discussions, we’ll learn to welcome the necessary mess, surprise, and even joy of the revision process. Finally, we’ll have multiple opportunities to share, to perform, to publish our own original pieces, and to enter writing competitions throughout the year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
    "Cyber Security": {
        "description": "This senior-year Software Engineering major course covers network security fundamentals, including data encryption, firewalls, and defensive scripting techniques used to protect systems from attack.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Design & Drafting for Production (DDP)": {
        "description": "This required freshman engineering course introduces students to the engineering design process through manual drafting and 3D CAD modeling in Autodesk Inventor. Students learn orthographic and isometric projection, dimensioning standards, and spatial reasoning skills by designing, modeling, and prototyping their own small products, building the drafting and design foundation used across every engineering major at Tech.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color" : req_courses
    },
    "Digital Animation": {
        "description": "This senior-year Media Communications major course covers animation fundamentals, including timeline-based motion, frame-by-frame techniques, and 3D character or object rigging.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Digital Design": {
        "description": "This senior-year Architecture major course builds on junior-year drafting skills, having students produce more advanced technical renderings and layouts using professional architectural design software. The course emphasizes precision, presentation quality, and translating design intent into buildable documentation.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Digital Electronics": {
        "description": "This introductory Electrical Engineering major course covers the design of logic systems using digital components, from basic logic gates through combinational and sequential circuits like adders, multiplexers, and flip-flops. Students test circuit designs in simulation software and on breadboards, and by spring semester extend into synchronous counters and state-machine design, with some classes programming FPGAs.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior"]
    },
    "Digital Media Arts & Adobe Photoshop": {
        "description": "This Media Communications major course builds core digital design skills using Adobe Photoshop, covering raster image editing, compositing, and visual design fundamentals such as layout, color, and typography. Students work toward an Adobe Photoshop industry certification as part of the coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Digital Photography": {
        "description": "This Media Communications major course covers photography fundamentals, including camera controls like aperture and exposure, composition, and digital post-processing and editing.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Digital Systems Design (Stony Brook Accredited)": {
        "description": "This senior-year Electrical Engineering major course, accredited through Stony Brook University, builds on junior-year digital electronics work by having students design more complex circuit systems, including simulated and programmed components built in Multisim. Projects include devices like BCD-to-seven-segment display decoders and arithmetic logic units, and many students also learn to solder through-hole components for hands-on circuit builds.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Drama": {
        "description": "This course is an exploration of dramatic literature through theatre of various genres, time periods and locales—from the ancient Greeks to Shakespeare to contemporary plays. We will investigate how dramatic literature shapes the times, and how the times shape dramatic literature through a mix of careful reading, critical discussion, literary analysis and on-your-feet, get-into-character dramatic performance.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },
    "Economics": {
        "description" : "This one-semester course introduces core economic principles, covering how individuals, businesses, and governments make decisions under scarcity, along with basic supply-and-demand analysis and an overview of the U.S. economic system.",
        "periods" : 1,
        "credits" : 1.0,
        "semesters" : 1,
        "is_elective" : False,
        "grades": ["Senior"],
        "color" : history_color
    },
    "Engineering Statics": {
        "description": "This junior-year Civil Engineering major course covers the analysis of forces on structures in equilibrium, including vector representation of forces, moments, trusses, and load distribution. It provides the structural-analysis foundation used in the major's senior-year certification coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "English 11": {
        "description" : "This rigorous, year-long course prompts eleventh-graders to examine how unique cultural, geographical, and historical identities are forged through diverse texts spanning the 17th to the 21st centuries. Students engage in close reading and analytical annotation of classic and contemporary novels, plays, essays, and primary source documents to critique thematic concepts like the evolution of the 'American Dream'. A strong emphasis is placed on advanced text-based writing, evidence-backed argumentation, and standard research methodologies. Ultimately, the course sharpens critical thinking and communication skills to prepare students for college-level writing, future career landscapes, and mandatory graduation requirements, including the NYS Regents Examination in English Language Arts.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"],
        "color": english_color
    },
    "English 10": {
        "description": "Building on English 9, this course centers on world literature, exploring texts from a range of cultures and time periods to examine universal themes such as identity, conflict, and justice. Students refine essay writing, rhetorical analysis, and discussion skills in preparation for the AP-level English courses available in junior and senior year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore"],
        "color": english_color
    },
    "English 9": {
        "description": "The first course in Tech's English sequence introduces students to major literary genres, including the short story, novel, drama, and poetry, while building foundational skills in grammar, vocabulary, and expository and analytical writing. Students learn to construct textual evidence-based arguments and develop close-reading habits that carry through the rest of the English curriculum.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color": english_color
    },
    "Environmental Sustainability": {
        "description": "This senior-year Environmental Science major course, based on the PLTW Environmental Sustainability curriculum, has students apply engineering and environmental science principles to sustainability projects, such as designing bat houses or green-roof models. Students also work on real building-level sustainability initiatives, including waste reduction, reuse, and energy conservation planning.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Film & Literature": {
        "description": "In Film & Literature, we will approach film as a text that deserves the same close reading and analysis that we give to literature. To this end, we will study and analyze how moving images of all kinds (e.g., narrative film, documentary, television, animation) create meaning and tell important stories even as they shape cultural values and reflect political and social contexts. We will examine how modes of storytelling have been adapted to fit the screen throughout modern history and across global cultures. As students develop film literacy, they will increase their capacity to watch films actively and critically, analyze film as a cultural phenomenon, question their own role as a spectator, and evaluate film as artistic expression, historical document, and ideological expression. Although we will enjoy watching a wide variety of films in this class, the course involves a substantial amount of reading (i.e., film theory, film criticism, works of literature that film is based on) and writing (i.e., scene analysis, personal responses, critical essays, research, screenplays).",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color": english_color
    },  
    "Finance & Investments": {
        "description": "This senior-year Finance major course covers investment fundamentals, including stocks, bonds, portfolio management, and market analysis, along with the basics of how capital markets function. Students often build and track simulated investment portfolios as part of the coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Flight School": {
        "description": "This Aerospace Engineering major course prepares students for the FAA Private Pilot Knowledge Exam, covering aerodynamics, aircraft systems, weather, navigation, airspace regulations, and flight planning. Students use flight simulators to apply what they learn about instrument navigation and flight procedures.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Forensic Criminology": {
        "description": "This senior-year Law & Society major course covers forensic science methods, including fingerprint and trace evidence analysis, alongside the psychology behind criminal behavior. In the last quarter of the year, students work in the school's forensics lab to analyze a simulated crime scene and present their findings in a mock trial in the courtroom.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "French I": {
        "description": "Introduces the fundamentals of the French language, focusing on present-tense high-frequency verbs, basic sentence structure, and conversational greetings. Students develop foundational listening and speaking skills while learning about the diverse cultures of the Francophone world.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman",  "Junior", "Senior"],
        "color" : lang_color
    },
    "French II": {
        "description": "Strengthens communicative proficiency by introducing past tenses and expanding vocabulary regarding travel, dining, and daily life. Students transition from writing isolated sentences to creating connected paragraphs and understanding authentic cultural media.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Sophomore"],
        "color" : lang_color
    },
    "French III": {
        "description": "Synthesizes advanced grammar, including the conditional and subjunctive moods, to prepare students for comprehensive language exams. Focuses on discussing abstract topics, reading short stories, and debating contemporary cultural trends across French-speaking nations.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore", "Junior"],
        "color" : lang_color
    },
    "Fundamentals of IT Infrastructure": {
        "description": "This junior-year Software Engineering major course covers IT infrastructure fundamentals, including networks and systems configuration.",
        "periods": 1,
        "semesters" : 1,
        "credits": 0.5,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Big Data: Warehousing and Analytics": {
        "description": "This junior-year Software Engineering major course covers big data warehousing and analytics, including how large datasets are stored, organized, and queried.",
        "periods": 1,
        "semesters" : 1,
        "credits": 0.5,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Fundamentals of Product Design": {
        "description": "This junior-year Industrial Design major course introduces the product design process, covering sketching, ergonomics, and user-centered design principles. It's the entry point into the Industrial Design sequence, building toward the major's senior-year modeling and certification coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Genetics": {
        "description": "This senior-year Biological Sciences major course, run in the school's dedicated DNA lab, explores modern genetics and molecular biology techniques such as DNA extraction, restriction enzyme analysis, gel electrophoresis, PCR, and bacterial transformation. Students also use bioinformatics tools to study DNA alignments and phylogenetic trees, building hands-on lab skills used in genetics and biotech fields.",
        "periods": 2,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Geometry": {
        "description": "This course covers Euclidean geometry with an emphasis on formal proof, congruence and similarity, coordinate geometry, circles, and geometric transformations. Students develop logical reasoning and proof-writing skills that are foundational for later math and physics coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color" : math_color
    },
    "German I": {
        "description": "Establishes core vocabulary and foundational grammar systems, including basic sentence structures and case endings. Students practice everyday conversational patterns, phonetic pronunciation, and explore the cultural landscapes of German-speaking Europe.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Junior", "Senior"],
        "color" : lang_color
    },
    "German II": {
        "description": "Expands structural language skills through past tenses, subordinate clauses, and specialized thematic vocabulary. Students learn to describe past events, express personal opinions, and navigate common transactional interactions in German.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Sophomore"],
        "color" : lang_color
    },
    "German III": {
        "description": "Refines complex syntactic structures and idiomatic expressions to build independent communicative confidence. Students read excerpted texts, debate societal topics, and analyze the historical and modern cultural impacts of the German-speaking world.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore", "Junior"],
        "color" : lang_color
    },
    "Graph Theory / Number Theory": {
        "description": "This Applied Mathematics major course spends one semester on Graph Theory and one semester on Number Theory. Graph Theory introduces topics starting with Leonhard Euler's famous Bridges of Konigsberg problem, the historical starting point of the field, then moves into isomorphic graphs, adjacency matrices, and Eulerian and Hamiltonian graphs. Students complete a culminating group presentation on a real-world application of graph theory. Number theory covers the basics of number theory, tracing the field back to some of its oldest known studies in Ancient China, through topics like the Euclidean Algorithm, the Fundamental Theorem of Arithmetic, and modular arithmetic via Fermat's Little Theorem, Euler's Theorem, and Wilson's Theorem. Modern applications such as cryptography and internet security are woven throughout, with Python used to supplement the material, and students also learn counting techniques from combinatorics before completing a culminating group presentation.",
        "periods" : 1,
        "credits": 2.0,
        "semesters" : 2,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Graphic Novels": {
        "description": "This course will take a critical and creative look at this popular genre. We will delve into the analysis of graphic novels as a literary form, exploring their visual storytelling techniques, narrative structures, thematic depth, and cultural impact. Along the way, we will read critical essays and traditional texts to enrich our understanding of graphic novels. Students will also develop their own graphic narrative creations through practice with character design, paneling, and sequential art.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },
    "Health Education": {
        "description" : "This one-semester required course covers personal and community wellness, including mental and emotional health, nutrition, substance abuse prevention, disease prevention, and healthy relationships. The class emphasizes practical decision-making skills students can apply to their own health and safety through high school and beyond.",
        "periods" : 1,
        "credits": 0.5,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Sophomore"],
        "color" : req_courses
    },
    "Human Anatomy": {
        "description": "This senior-year Biological Sciences major course studies human anatomy and physiology system by system, covering all eleven body systems through lecture, models, and hands-on lab work. Students perform dissections, examine tissue slides under the microscope, take vital-sign measurements, and build anatomical models, approaching the material through a medical lens.",
        "periods": 2,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Introduction to Business Law": {
        "description": "This senior-year Finance major course introduces the legal framework behind business operations, including contracts, corporate structures, and commercial liability. It's generally considered less math-intensive than the major's economics coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Math Research & Python Programming": {
        "description": "This junior-year Applied Mathematics major course introduces students to thinking, writing, and presenting mathematics, building from a series of small writing assignments up to two full-length mathematical research papers, one each in the fall and spring terms. Students work throughout the year with current Junior and Senior Math majors and the major's teachers, present their findings to the class, and submit their papers to the NYC Metropolitan Math Fair and other research competitions.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Introduction to Neuroscience": {
        "description": "This senior-year Neuroscience major course introduces the structure and function of the nervous system, covering neuron and brain cell biology and how the brain processes sensory information and generates behavior.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Inventor Certification": {
        "description": "This senior-year Industrial Design major course prepares students for the Autodesk Inventor professional certification exam, reinforcing precise mechanical CAD modeling skills used throughout the major.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Italian I": {
        "description": "An introductory course focusing on correct pronunciation, essential noun-adjective agreements, and basic conversational vocabulary. Students practice speaking about family, school, and interests while gaining exposure to Italy's rich geography and cultural traditions.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman",  "Junior", "Senior"],
        "color" : lang_color
    },
    "Italian II": {
        "description": "Builds upon foundational skills by introducing past tenses, reflexive verbs, and situational vocabulary for navigating Italian life. Students improve reading comprehension through brief narratives and develop more cohesive paragraph-length writing.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Sophomore"],
        "color" : lang_color
    },
    "Italian III": {
        "description": "Prepares students for advanced assessments by exploring compound tenses, pronoun systems, and refined literary vocabulary. The curriculum emphasizes continuous target-language discussions on historical milestones, arts, and contemporary lifestyle dynamics in Italy.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore", "Junior"],
        "color" : lang_color
    },
    "Journalism": {
        "description": "The study of journalism is both about the work of journalists and the way that work shapes an average reader's understanding and experience of their world. The focus of this course is both on practice of journalism and the discussion of current events that will be informed by our reading of journalistic writing. We begin our year with the big picture: what is journalism and why is it important? Next, we learn how to be critical readers of journalism, and how to engage in source-based civil conversation about current events and social issues. Thereafter, there is a once-weekly focus on current event discussions. Our units will continue to 'zoom in' on specific areas of journalistic writing such as hard-news writing and opinion-editorial writing. We will also 'zoom out' to study how other sources of media (including entertainment-media & social) shape our understanding of the world. You may engage with other areas of journalism including but not limited to photojournalism, travel journalism, podcast & audio journalism, and/or magazine writing & design.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
    "Linear Algebra": {
        "description": "Linear Algebra is both an important branch of pure mathematics and a fundamental component of applications spanning finance, cryptography, stochastic processes, web search, machine learning, and image processing. This senior-year Applied Mathematics major course covers the basic elements of a college-level introduction to linear algebra, including matrix algebra, determinants, elementary vector spaces, and characteristic equations and eigenvalues, and students use computing technologies to build and explore applications of the material as time allows.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "available_grades": ["Senior"],
        "color" : math_color
    },
    "Live, Love, & Death": {
        "description": "These three concepts are the pillars of our existence and are, by definition, present in all literature. This course explores how the search for identity, purpose and love helps to define a person. Over the course of the year, as we explore the connections among the concepts of life, love, and death, we will read and analyze texts about which students will make personal, real-world, and academic connections by engaging in a variety of tasks: research, personal essays, literary analysis, dramatic presentations and public speaking. The course will cover a wide range of texts from a number of time periods and perspectives in order to explore some the following philosophical questions: What makes life worth living? What keeps us going in the toughest of times? How does love drive us, power us, throughout our lives? How does death affect us? How do people move forward from traumatic experiences? How do we rebuild? How do all of these concepts define us individually and also affect humanity as a whole? Texts vary but may include: Oedipus the King, Antigone, Othello, Twelfth Night, The Stranger, Beloved, Angela’s Ashes, Everything I Never Told You, The Things They Carried, and postmodern short stories along with selected poetry and essays.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
    "Math Team Class": {
        "description": "This pass/fail class supports students preparing for competitive mathematics tournaments, covering advanced problem-solving strategies in areas like algebra, geometry, combinatorics, and number theory beyond the standard curriculum. It's open to students across all grade levels who compete on Tech's math team.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Freshman", "Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Mechatronics with LabView": {
        "description": "This senior-year Mechatronics & Robotics major course covers industrial control systems and instrumentation using National Instruments' LabVIEW graphical programming environment, building on the robotics and electronics skills developed junior year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Methods of Fabrication": {
        "description": "This junior-year Industrial Design major course teaches hands-on fabrication techniques using traditional woodworking tools alongside modern rapid-prototyping equipment like 3D printers and laser cutters. Students learn to translate product designs into physical prototypes.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Mobile Application Development": {
        "description": "This senior-year Software Engineering major course has students design and build mobile apps, covering interactive app interfaces, deployment, and managing user data and app state.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Modern Instrumental Chemical Analysis": {
        "description": "Also known as MICA, this senior-year, one-period, one-semester Chemistry major course has students explore the rotational, vibrational, and electronic states of atoms and molecules and how radiation interacts with them, along with molecular symmetry and electronic, rotational, and vibrational spectroscopy. Students learn to identify chemical compounds through joint application of spectroscopic techniques such as IR, H-NMR, C13-NMR, mass spectrometry, and UV spectroscopy.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Modern Physics": {
        "description": "This course moves beyond classical mechanics to cover 20th-century physics, including atomic structure, quantum behavior, and special relativity.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior","Senior"]
    },
    "Multivariable Calculus": {
        "description": "Multivariable Calculus extends the core ideas of calculus, derivatives and integrals, into three-dimensional space by introducing functions of several variables. Students learn to model systems where multiple quantities change simultaneously, such as curved surfaces, vector fields, and fluid or spatial forces, using tools like partial derivatives, multiple integrals, and vector calculus. This college-level course is a common requirement for university tracks in engineering, physics, computer science, and data science.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "available_grades": ["Senior"],
        "color" : math_color
        
    },
    "Mystery, Horror & the Supernatural": {
        "description": " The spooky, the creepy, and the unexplainable will be common threads through your reading and writing in this course as well as the inspiration for discussions, presentations and creative projects. Though the course is thematically similar for each teacher, texts and critical lenses vary wildly. You might explore Bram Stoker’s Dracula or you could be taking a deep-dive into Toni Morrison’s Beloved. In some classes, you’ll read short stories; in others, you’ll write them. We use a variety of critical lenses, with some favorites being queer theory, post-colonialism, feminism, reader-response, and psychoanalytic theory. These lenses will drive discussion of how authors develop fear and discomfort in their audience while simultaneously addressing social issues. If you’re ready to dive into the various ways horror is presented, created, and kept relevant, then this is the course for you! Note: This course does not have NCAA accreditation; students who anticipate pursuing NCAA athletics in college should not list this course as a preference.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
    "Orchestra": {
        "description": "This pass/fail performing ensemble class develops string and instrumental technique through the rehearsal and performance of orchestral repertoire spanning classical and contemporary works. It's open to students in any grade and can be taken more than once.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Freshman", "Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Organic Chemistry": {
        "description": "This senior-year, one-semester double-period Chemistry major course covers the chemistry of organic molecules, including the structure, nomenclature, properties, and reactions of carbon compounds with an emphasis on aliphatic compounds, along with an introduction to reaction mechanisms and stereochemistry. The course includes lab work on the preparation, isolation, and purification of typical organic compounds, with experiments chosen to illustrate basic organic chemistry techniques.",
        "periods" : 2,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Organic Chemistry Pharmacy Seminar": {
        "description": "This senior-year LIU Pharmacy major course, run as a double period, applies organic chemistry concepts to pharmaceutical topics such as drug structure and bonding, connecting classroom chemistry to real pharmacy practice as part of the major's partnership with LIU's pharmacy program.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "PLTW Aerospace Engineering": {
        "description": "A Project Lead The Way specialization course for the Aerospace Engineering major, this class explores the physics and engineering behind atmospheric and space flight, including aerodynamics, propulsion, orbital mechanics, and materials used in aerospace design. Students apply these concepts through design challenges and simulations.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "PLTW Civil Engineering & Architecture": {
        "description": "A Project Lead The Way specialization course, this class introduces the fundamentals of building and site design, having students apply math, science, and standard engineering practices to design residential and commercial projects. Students develop skills in engineering calculations, technical documentation, and 3D architectural modeling and design software as they work through structured design problems.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "PLTW Computer Integrated Manufacturing": {
        "description": "A Project Lead The Way specialization course, this class covers automated manufacturing systems, including CNC machining, robotics, and computer-integrated production processes. Students design parts and translate those designs into manufactured products using the school's laser cutters, 3D printers, and CNC equipment.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "PLTW Digital Electronics": {
        "description": "A Project Lead The Way specialization course for the Electrical Engineering major, this class covers digital logic design, including combinational and sequential circuits, using both simulation software and physical circuit-building. It's the junior-year entry point into the Electrical Engineering sequence, building directly on skills used in Digital Systems Design senior year.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior", "Senior"]
    },
    "PLTW Principles of Engineering": {
        "description": "A Project Lead The Way foundational course, this class exposes students to major engineering topics including mechanisms, energy, statics, materials, and manufacturing processes through hands-on projects and problem-solving activities. It builds broad engineering literacy that underlies the more specialized PLTW courses taken later in the Aerospace Engineering major.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Participation in Government": {
        "description" : "This one-semester course examines how government works in practice at the local, state, and federal levels, covering topics such as civic institutions, the legislative process, elections, and public policy formation. This course is by default taken during the same year as Economics, each being one semester long.",
        "periods" : 1,
        "credits" : 1.0,
        "semesters" : 1,
        "is_elective" : False,
        "grades": ["Senior"],
        "color" : history_color
    },
    "Pre-Calculus": {
        "description": "This course prepares students for calculus by deepening their study of polynomial, rational, exponential, logarithmic, and trigonometric functions, along with sequences, series, and an introduction to limits. It's the standard bridge between Algebra II and AP Calculus AB or BC.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore","Junior"],
        "color" : math_color
    },
    "Pre-AP World History": {
        "description": "The Pre-AP World History course is a year-long class that explores the economic, political, and cultural movements that shaped the global community from ancient civilizations to the modern era. Developed by the College Board, the curriculum emphasizes deep historical analysis over rote memorization, prompting students to evaluate primary sources, track geographic changes, and identify long-term patterns of continuity and change across different regions. By focusing on critical reading, evidence-based writing, and structured data analysis, the course serves as a rigorous foundational pathway that prepares students for success in future Advanced Placement (AP) social studies classes.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color" : history_color
    },
    "Principles of Accounting": {
        "description": "This junior-year Finance major course introduces core accounting concepts, including financial statements, the accounting cycle, and ledger and journal entry processing. It provides the financial-literacy foundation used throughout the rest of the Finance major's coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Quantitative Analysis": {
        "description": "This senior-year, one-semester double-period Chemistry major course introduces the principles and calculations of quantitative analysis, covering chemical stoichiometry, acid and base concepts, ionic equilibria, acid-base titrations, spectrophotometry, oxidation-reduction reactions, complex compounds, gravimetric analysis, and precipitation titrations. Lab work covers elementary gravimetric, volumetric, and instrumental analysis, with an emphasis on applying these concepts to forensic chemistry and forensic analysis.",
        "periods" : 2,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Regents Biology": {
        "description": "The Regents Biology course is a mandatory, year-long high school class that explores the fundamental principles of life, cellular structures, and the interconnectedness of ecosystems. Following the New York State science learning standards, the curriculum covers core biological concepts including genetics, evolution, human anatomy, reproduction, and the impact of human activity on the biosphere. Students participate in hands-on laboratory investigations to satisfy the state's mandatory 1,200-minute lab requirement, developing critical skills in scientific inquiry, data analysis, and experimental design. The course equips students with the scientific literacy needed for modern global challenges and directly prepares them to pass the mandatory New York State Regents Examination.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color" : science_color
    },
    "Regents Chemistry": {
        "description": "This required physical-setting chemistry course covers atomic theory, the periodic table, bonding, stoichiometry, chemical reactions, and the states of matter, aligned to the NY Regents Chemistry curriculum. The course includes a mandatory lab component (often run as a double period) where students practice quantitative lab technique ahead of AP-level science electives.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore"],
        "color" : science_color
    },
    "Regents Global History": {
        "description": "This survey course traces world history from early civilizations through the modern era, examining political, economic, social, and cultural developments across regions. Students build skills in document-based analysis and historical argumentation used throughout Tech's social studies sequence.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman"],
        "color" : history_color
    },
    "Regents Physics": {
        "description": "This required physical-setting physics course introduces mechanics, waves and sound, electricity and magnetism, and modern physics topics at an algebra-based level, aligned to the NY Regents Physics curriculum. Lab work, run in double periods, has students collecting and analyzing real experimental data, building the base for AP Physics I and beyond.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Junior"],
        "color" : science_color
    },
    "Regents US History": {
        "description": "The United States History Regents course is a mandatory, year-long 11th-grade class that explores the major political, economic, and social turning points that shaped America from the colonial era to the modern day. Following the New York State Social Studies Framework, the curriculum focuses on key historical eras, including the American Revolution, the Civil War, industrialization, the World Wars, and modern civil rights movements. Rather than relying on simple memorization, students develop critical historical thinking skills by analyzing primary sources, evaluating conflicting perspectives, and tracking continuity and change over time. The course actively builds the reading, source-analysis, and essay-writing skills required to pass the mandatory New York State Regents Examination at the end of the school year.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"],
        "color" : history_color
    },
    "Robotics Engineering": {
        "description": "This junior-year Mechatronics & Robotics major course is a multidisciplinary introduction to mechatronics, having students build robotic devices with VEX hardware while learning mechanical design, electronics, and control systems. Students program their robots using languages like C, Arduino, RobotC, and easyC, culminating in a mechatronic device that solves a real-world problem.",
        "periods": 2,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Science Fiction & Fantasy": {
        "description": "This genre-specific class dives right into the big questions: Why are science fiction and fantasy appealing and what are their origins? How does a journey in an unreal world inform and influence our perspective of the “real” world? How does the creation of alternate realities create a safe space for authors to discuss their social, political, and cultural realities? How do science-fiction and fantasy texts build upon classical texts for inspiration and themes? We explore some of these questions in our encounters with dystopian worlds and outer-space, mythologies and modern fantasy. Text selection varies but may include works by the following authors: Margaret Atwood, Neil Gaiman, J.R.R. Tolkien, Mary Shelley, Isaac Asimov, Phillip K. Dick, Octavia Butler, Ken Liu, Rebecca Roanhoarse, Ray Bradbury, Ursula K. Le Guinn, student-selected books and many others. Emphasis is placed on literary analysis and expository writing, but the class also includes opportunities for speeches, individual and group presentations/lessons, creative writing and artwork.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
    "Social Science Research": {
        "description": "This senior-year capstone course for the Social Science Research major has students complete a year-long independent research paper on a topic of their choosing in the social sciences or history. The fall semester builds information literacy and source-evaluation skills using databases like JSTOR and ProQuest, while the spring semester is devoted to writing, with strong papers eligible for publication in the school's student research journal.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Sociology": {
        "description": "This junior-year Social Science Research major course examines the structure of society, covering topics such as social class, institutions, and how cultures and communities change over time.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Spanish I": {
        "description": "A beginner-level course establishing core present-tense structures, essential vocabulary, and functional speech patterns. Students build conversational confidence for daily interactions while discovering the vibrant cultures and traditions of the Spanish-speaking world.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Junior", "Senior"],
        "color" : lang_color
    },
    "Spanish II": {
        "description": "Enhances communication skills by incorporating preterite and imperfect past tenses alongside expanded thematic units. Students read simple authentic texts, write short creative passages, and describe personal experiences with increasing fluency.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Freshman", "Sophomore"],
        "color" : lang_color
    },
    "Spanish III": {
        "description": "Solidifies advanced grammatical frameworks, including the future tense and subjunctive mood, to prepare students for proficiency exams. Focuses on contextual speaking, reading short literary works, and analyzing contemporary social themes across Hispanic communities.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Sophomore", "Junior"],
        "color" : lang_color
    },
    "Student Leadership": {
        "description": "This pass/fail elective develops practical leadership skills through hands-on experience with project management, community service coordination, and school event planning. It's open to students in any grade and can be taken more than once.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Freshman", "Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Studio Art": {
        "description": "Studio Art is a foundational, hands-on visual arts course that introduces students to essential drawing, painting, and design techniques while exploring the core elements of line, color, and composition. Through regular studio projects, sketchbook exercises, and group critiques, students learn to translate visual ideas into finished works, build technical proficiency across various traditional mediums, and develop their own personal artistic voice.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior","Senior"]
    },
    "Surveying Certification": {
        "description": "This senior-year Civil Engineering major course covers land surveying fundamentals, including coordinate systems, measurement instruments, and grading and site layout, preparing students for an industry-recognized surveying certification such as through the National Society of Professional Surveyors.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Video Game Design with Unity": {
        "description": "This junior-year Media Communications major course teaches game development using the Unity engine, covering asset placement, scripting, and interactive movement and gameplay mechanics.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Junior"]
    },
    "Virtual Enterprise": {
        "description": "This senior-year Finance major course has students run a simulated company as part of the global Virtual Enterprises International network, taking on employee and executive roles to manage operations, finances, and marketing in a simulated marketplace. It's a hands-on, project-based capstone to the Finance major's business coursework.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": True,
        "grades": ["Junior", "Senior"]
    },
    "Web Development": {
        "description": "This senior-year Software Engineering major course covers front-end web development, including page layout, styling, and building interactive page components and user interfaces.",
        "periods" : 1,
        "credits": 1.0,
        "semesters": 1,
        "is_elective": False,
        "grades": ["Senior"]
    },
    "Weston Research": {
        "description": "Part of the Weston Research Scholars Program, this pass/fail class has sophomores, juniors, and seniors work independently or in small groups, under a research-experienced teacher, to develop an original research question and carry out a project intended for science and engineering competitions or peer-reviewed publication. Students build literature-review, experimental design, and scientific writing skills over the course of the program, often including independent summer work.",
        "periods": 1,
        "credits": 0.0,
        "is_elective": True,
        "available_grades": ["Sophomore", "Junior", "Senior"],
        "allow_multiple": True
    },
    "Yearbook": {
        "description": "This class is a year-long project-based course in which the class envisions, designs, and creates the yearbook for the senior class. Participants collaborate to capture all aspects of student life in this memorable publication. The yearbook staff work as a team, building skills of design and layout, photography, journalism, and copyediting. The course requires a substantial time commitment, particularly around deadlines, and yields a book that will last a lifetime.",
        "periods": 1,
        "credits": 1.0,
        "is_elective": False,
        "grades": ["Senior"],
        "color" : english_color
    },  
#non classes
    "Lunch" : {
        "description" : "Mandatory free period that cannot be swapped for a class period. During free periods, students usually spend time in the cafeteria, library, or auditorium.",
        "periods" : 1,
        "credits" : 0.0,
        "is_elective" : False,
        "grades" : ["Freshman", "Sophomore", "Junior", "Senior"],
        "color" : gym_lunch_color,
        "lunch_or_gym" : True,
    },

    "Physical Education" :{
        "description" : "At Brooklyn Tech, this period is spent in different ways on different days. P.E. occurs on all even or all odd days, depending on the students schedule. This equates to having P.E. 2 or 3 times a week. If you are taking a science class, you have a lab period once a week during this period. Each year for a semester, you will have advisory once a week during this period. Otherwise, this period is a free period.",
        "periods" : 1,
        "credits" : 0.0,
        "is_elective" : False,
        "grades" : ["Freshman", "Sophomore", "Junior", "Senior"],
        "color" : gym_lunch_color,
        "lunch_or_gym" : True,
    }
}


AP_COURSES = [
    "AP African American Studies",
    "AP Biology",
    "AP Business with Personal Finance",
    "AP Calculus AB",
    "AP Calculus BC",
    "AP Capstone Research",
    "AP Capstone Seminar",
    "AP Chemistry",
    "AP Chinese Language & Culture",
    "AP Comparative Government",
    "AP Computer Science Applications - JAVA",
    "AP Computer Science Principles",
    "AP Cybersecurity",
    "AP English Language & Composition",
    "AP English Literature & Composition",
    "AP Environmental Science",
    "AP European History",
    "AP French Language & Culture",
    "AP German Language & Culture",
    "AP Human Geography",
    "AP Italian Language & Culture",
    "AP Macroeconomics / AP Microeconomics",
    "AP Macroeconomics with Government",
    "AP Physics C: Electricity & Magnetism",
    "AP Physics C: Mechanics",
    "AP Physics I",
    "AP Physics II",
    "AP Psychology",
    "AP Spanish Language & Culture",
    "AP Statistics",
    "AP Studio Art 2D",
    "AP US Government",
    "AP US History",
    "AP World History",
]