"""In-memory lesson catalog used by the /lesson/<id> route.

Later you can replace this with database models.
"""

from __future__ import annotations

LESSONS = {
    "basic-algebra": {
        "id": "basic-algebra",
        "title": "Basic Algebra & Ratios",
        "level_label": "Middle School",
        "subject_label": "Mathematics",
        "description": "Learn core operational structures including simple algebraic expressions, linear equations, percentages, and ratios.",
        "videos": [
            {
                "id": "NybHckSEQBI",
                "label": "Part 1: Introduction (Algebra Basics: What Is Algebra?)",
            },
            {
                "id": "kWOTmyoaWJg",
                "label": "Part 2: Practice Examples (Solving Basic Equations)",
            },
            {
                "id": "V3dFHt9p5W8",
                "label": "Part 3: Test (Algebra Basic Lessons for Beginners)",
            },
        ],
        "notes_bullets": [
            "Translate word problems into algebraic expressions.",
            "Use ratios and percentages to compare quantities.",
            "Practice simplifying equations step-by-step.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.scribd.com/document/823007092/Basic-Algebra-Worksheet",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://mathsux.org/wp-content/uploads/2021/05/Algebra-Cheat-Sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "trigonometry-foundations": {
        "id": "trigonometry-foundations",
        "title": "Trigonometry Foundations",
        "level_label": "High School • G10",
        "subject_label": "Mathematics",
        "description": "Understanding sine, cosine, tangent laws, and basic trigonometric identities inside right triangles.",
        "videos": [
            {
                "id": "PUB0TaZ7bhA",
                "label": "Part 1: Introduction (Trigonometry For Beginners)",
            },
            {
                "id": "GtpplO7xdqM",
                "label": "Part 2: Practice Examples (Trigonometry made easy)",
            },
            {
                "id": "erQFfES-njE",
                "label": "Part 3: Test (All Of Trigonometry Explained In 12 Minutes)",
            },
        ],
        "notes_bullets": [
            "Identify the opposite/adjacent/hypotenuse sides.",
            "Use SOH-CAH-TOA to solve right triangle problems.",
            "Connect triangle ratios with basic identities.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Trigonometry Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.mathworksheets4kids.com/trigonometry/basic-ratios-all1.pdf",
            },
            {
                "type": "pdf",
                "label": "Trigonometry Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://tutorial.math.lamar.edu/pdf/Trig_Cheat_Sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "statistics-probability": {
        "id": "statistics-probability",
        "title": "Statistics & Probability",
        "level_label": "High School • G11",
        "subject_label": "Mathematics",
        "description": "Analyze data sets, standard deviation, variance, and predict outcomes using permutation and combination laws.",
        "videos": [
            {
                "id": "kyjlxsLW1Is",
                "label": "Part 1: Introduction (Teach me STATISTICS in half an hour)",
            },
            {
                "id": "YTWM4aOqVwM",
                "label": "Part 2: Practice Examples (Probability: The Basics EXPLAINED)",
            },
            {
                "id": "LgLgexX7iTs",
                "label": "Part 3: Test (Probability Top 10 Must Knows)",
            },
        ],
        "notes_bullets": [
            "Compute mean/variance and interpret the results.",
            "Apply probability rules for events and outcomes.",
            "Use combinations/permutations for counting problems.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Statistics and Probability Exercises",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.mathworksheets4kids.com/statistics/mean-median-mode-range-all1.pdf",
            },
            {
                "type": "pdf",
                "label": "Probability Formulas Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.probabilitycourse.com/downloads/probability_cheat_sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "calculus-limits": {
        "id": "calculus-limits",
        "title": "Essential Calculus Limits",
        "level_label": "High School • G12",
        "subject_label": "Mathematics",
        "description": "Learn foundational limits properties, continuous derivatives theories, and absolute boundary proofs.",
        "videos": [
            {
                "id": "YNstP0ESndU",
                "label": "Part 1: Introduction (Calculus 1 - Introduction to Limits)",
            },
            {
                "id": "PuVuNRqsNW0",
                "label": "Part 2: Practice Examples (3 WAYS TO SOLVE LIMITS)",
            },
            {
                "id": "rnd9FYWSpgY",
                "label": "Part 3: Test (Complete Guide to Limits in Calculus 1)",
            },
        ],
        "notes_bullets": [
            "Understand limit meaning and notation.",
            "Use limit laws to evaluate expressions.",
            "Practice continuity and derivative ideas.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Limits Practice Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.mathworksheets4kids.com/calculus/limits-basic.pdf",
            },
            {
                "type": "pdf",
                "label": "Calculus Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://tutorial.math.lamar.edu/pdf/Calculus_Cheat_Sheet_All.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "intro-ecosystems": {
        "id": "intro-ecosystems",
        "title": "Introduction to Ecosystems",
        "level_label": "Middle School",
        "subject_label": "Science & Physics",
        "description": "Discover basic environmental factors, energy cycles, food chains, and interactive ecological balances.",
        "videos": [
            {
                "id": "KQF9WdZrH_c",
                "label": "Part 1: Introduction (What Are Ecosystems? - Crash Course Geography)",
            },
            {
                "id": "7cRgK0qG00E",
                "label": "Part 2: Practice Examples (What is an ecosystem?)",
            },
            {
                "id": "sKJoXdrOT70",
                "label": "Part 3: Test (ECOSYSTEM - The Dr. Binocs Show)",
            },
        ],
        "notes_bullets": [
            "Define ecosystems and identify components.",
            "Explain energy flow using food chains.",
            "Describe how ecosystems maintain balance.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Ecosystems Study Guide",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.biologycorner.com/worksheets/ecology-basics.pdf",
            },
            {
                "type": "pdf",
                "label": "Fundamentals of Ecology Module",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/nrcs142p2_051336.pdf",
            },
            {
                "type": "pdf",
                "label": "Ecosystem Energy Flow Overview",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.biologyman.com/uploads/Ecology_Cheat_Sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "cellular-biology-genetics": {
        "id": "cellular-biology-genetics",
        "title": "Cellular Biology & Genetics",
        "level_label": "High School • G10",
        "subject_label": "Science & Physics",
        "description": "Understand the structure of animal/plant cells, DNA replication, and fundamental Mendelian genetics.",
        "videos": [
            {
                "id": "URUJD5NEXC8",
                "label": "Part 1: Introduction (Biology: Cell Structure)",
            },
            {
                "id": "8m6hHRlKwxY",
                "label": "Part 2: Practice Examples (DNA, Chromosomes, Genes, and Traits)",
            },
            {
                "id": "Z6O_5Noh4WM",
                "label": "Part 3: Test (Introduction to Genetics - DNA, RNA, Genes)",
            },
        ],
        "notes_bullets": [
            "Compare plant and animal cell structures.",
            "Summarize DNA replication at a high level.",
            "Apply Mendelian genetics to basic inheritance.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Cell Biology Study Module",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.nature.com/scitable/topicpage/the-cell-14022648/",
            },
            {
                "type": "pdf",
                "label": "Genetics Fundamentals Guide",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.genome.gov/genetics-glossary",
            },
            {
                "type": "pdf",
                "label": "DNA and Genetics Overview",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.khanacademy.org/science/high-school-biology/hs-molecular-genetics",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "organic-chemistry-structure": {
        "id": "organic-chemistry-structure",
        "title": "Organic Chemistry Structure",
        "level_label": "High School • G11",
        "subject_label": "Science & Physics",
        "description": "Explore hydrocarbons formations, functional chemical groups, and common industrial reaction frameworks.",
        "videos": [
            {
                "id": "HRz-jH4CAy8",
                "label": "Part 1: Introduction (Organic Chemistry Introduction Part 1)",
            },
            {
                "id": "bFn-OjeWNAw",
                "label": "Part 2: Practice Examples (Drawing Structures: Bond Line, Skeletal)",
            },
            {
                "id": "B_ketdzJtY8",
                "label": "Part 3: Test (Organic Chemistry - Basic Introduction)",
            },
        ],
        "notes_bullets": [
            "Recognize functional groups and their properties.",
            "Understand basic hydrocarbon families.",
            "Connect structure to typical reactions.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Organic Chemistry Structures Overview",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.masterorganicchemistry.com/downloads/Orgo-Cheat-Sheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Lewis Structures Practice",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://www.chem.ucla.edu/~harding/IGOC/L/lewis_structure.pdf",
            },
            {
                "type": "pdf",
                "label": "Hybridization and Bonding Reference",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/19532658b09d0208221805553e16b907_bond_str.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "quantum-physics-intro": {
        "id": "quantum-physics-intro",
        "title": "Quantum Physics Intro",
        "level_label": "High School • G12",
        "subject_label": "Science & Physics",
        "description": "Explore photo-electric effects, wave-particle dualities, blackbody radiation concepts, and modern atomic theories.",
        "videos": [
            {
                "id": "p9pPjASnnxw",
                "label": "Part 1: Introduction (Quantum Mechanics Explained in Ridiculously Simple Words)",
            },
            {
                "id": "7kb1VT0J3DE",
                "label": "Part 2: Practice Examples (Quantum Mechanics - Crash Course Physics Part 1)",
            },
            {
                "id": "Usu9xZfabPM",
                "label": "Part 3: Test (If You Don't Understand Quantum Physics, Try This!)",
            },
        ],
        "notes_bullets": [
            "Introduce quantum ideas with real-world examples.",
            "Explain wave-particle duality.",
            "Describe blackbody radiation and its significance.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "reading-comprehension": {
        "id": "reading-comprehension",
        "title": "Reading Comprehension Skills",
        "level_label": "Middle School",
        "subject_label": "English & Linguistics",
        "description": "Enhance basic text analysis, plot structure identification, and essential vocabulary development.",
        "videos": [
            {
                "id": "8Y8Mb2RuvDM",
                "label": "Part 1: Introduction (Mastering Reading Comprehension Skills)",
            },
            {
                "id": "dPvWRYPadFg",
                "label": "Part 2: Practice Examples (3 Effective Strategies to Ace RC)",
            },
            {
                "id": "W7BW9gv_OkU",
                "label": "Part 3: Test (Reading comprehension strategies & tips)",
            },
        ],
        "notes_bullets": [
            "Use context clues for unfamiliar words.",
            "Identify main idea and supporting details.",
            "Practice predicting and summarizing.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "public-speaking-debate": {
        "id": "public-speaking-debate",
        "title": "Public Speaking & Debate",
        "level_label": "High School • G10",
        "subject_label": "English & Linguistics",
        "description": "Learn effective non-verbal techniques, constructive argumentation structures, and refutation strategies.",
        "videos": [
            {
                "id": "i5mYphUoOCs",
                "label": "Part 1: Introduction (Public Speaking For Beginners)",
            },
            {
                "id": "Cry_rcxSiCc",
                "label": "Part 2: Practice Examples (Public Speaking and Debating for Beginners)",
            },
            {
                "id": "-FOCpMAww28",
                "label": "Part 3: Test (TED's secret to great public speaking)",
            },
        ],
        "notes_bullets": [
            "Plan speeches with clear structure.",
            "Practice persuasive language and body control.",
            "Use evidence to support claims in debates.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "american-lit-poetry": {
        "id": "american-lit-poetry",
        "title": "American Literature & Poetry",
        "level_label": "High School • G11",
        "subject_label": "English & Linguistics",
        "description": "Analyze classic literary works, interpret poetic devices, and understand historical contexts in literature.",
        "videos": [
            {
                "id": "ZuFiERy7RL0",
                "label": "Part 1: Introduction (Intro to Early American Literature)",
            },
            {
                "id": "o3x-g5qRCYw",
                "label": "Part 2: Practice Examples (Analyze ANY Poem With These Steps!)",
            },
            {
                "id": "fbK72UkUCV4",
                "label": "Part 3: Test (How to Analyze and Annotate ANY Poem!)",
            },
        ],
        "notes_bullets": [
            "Spot literary devices and explain their effects.",
            "Connect themes with historical context.",
            "Practice close reading of poems.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "academic-essay-writing": {
        "id": "academic-essay-writing",
        "title": "Academic Essay Writing",
        "level_label": "High School • G12",
        "subject_label": "English & Linguistics",
        "description": "Master comprehensive bibliographic standards, logical argument flows, and systematic citation architectures.",
        "videos": [
            {
                "id": "UuOWNNvupik",
                "label": "Part 1: Introduction (How to Write an Essay: 4 Minute Step-by-step Guide)",
            },
            {
                "id": "tBAbIobh3uo",
                "label": "Part 2: Practice Examples (How to Write an Academic Essay in 10 Minutes)",
            },
            {"id": "liyFKUFCQno", "label": "Part 3: Test (How to write a good essay)"},
        ],
        "notes_bullets": [
            "Build thesis statements and logical paragraphs.",
            "Use citations properly and consistently.",
            "Revise for clarity, grammar, and structure.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "visual-logic-scratch": {
        "id": "visual-logic-scratch",
        "title": "Visual Logic & Scratch",
        "level_label": "Middle School",
        "subject_label": "Computer Science & IT",
        "description": "Learn basic algorithmic thinking, sequence creation, and loop conditions using interactive block programming.",
        "videos": [
            {
                "id": "D-nW4jvzRr8",
                "label": "Part 1: Introduction (Beginners Guide To Scratch)",
            },
            {
                "id": "zOa5o9Yq_ZU",
                "label": "Part 2: Practice Examples (Scratch Basics - Beginners Guide)",
            },
            {
                "id": "pU2TtjFzAJY",
                "label": "Part 3: Test (ALL Scratch Blocks in 5 MINUTES!!)",
            },
        ],
        "notes_bullets": [
            "Think in steps: inputs → processes → outputs.",
            "Use loops to repeat tasks efficiently.",
            "Debug by checking each block behavior.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "python-fundamentals": {
        "id": "python-fundamentals",
        "title": "Python Fundamentals",
        "level_label": "High School • G10",
        "subject_label": "Computer Science & IT",
        "description": "Master Python syntax, variables, conditionals, arrays, and writing clean, efficient code scripts.",
        "videos": [
            {
                "id": "QoIRX37VZpo",
                "label": "Part 1: Introduction (What is Python? Explained in 2 Minutes)",
            },
            {
                "id": "Ro_MScTDfU4",
                "label": "Part 2: Practice Examples (Learn Python in Only 30 Minutes)",
            },
            {
                "id": "kqtD5dpn9C8",
                "label": "Part 3: Test (Python for Beginners - Learn Coding in 1 Hour)",
            },
        ],
        "notes_bullets": [
            "Use variables with clear naming conventions.",
            "Practice if/else branching and loops.",
            "Write small functions for reusable logic.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "frontend-web-dev": {
        "id": "frontend-web-dev",
        "title": "Frontend Web Development",
        "level_label": "High School • G11",
        "subject_label": "Computer Science & IT",
        "description": "Build responsive websites from scratch using HTML5, modern CSS3 (Flexbox/Grid), and introductory JavaScript.",
        "videos": [
            {
                "id": "Tef1e9FiSR0",
                "label": "Part 1: Introduction (The Complete Frontend Developer Roadmap)",
            },
            {
                "id": "TG6XSFeOT3g",
                "label": "Part 2: Practice Examples (How I'd Learn Web Development)",
            },
            {
                "id": "GxmfcnU3feo",
                "label": "Part 3: Test (The Complete Web Development Roadmap)",
            },
        ],
        "notes_bullets": [
            "Structure pages with semantic HTML.",
            "Use Flexbox/Grid for responsive layouts.",
            "Add interactive behavior with basic JavaScript.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "backend-frameworks-sql": {
        "id": "backend-frameworks-sql",
        "title": "Backend Frameworks & SQL",
        "level_label": "High School • G12",
        "subject_label": "Computer Science & IT",
        "description": "Understand modular dynamic logic structures, relational database connection scripts, and CRUD data flows safely.",
        "videos": [
            {
                "id": "OeEHJgzqS1k",
                "label": "Part 1: Introduction (The Complete Backend Developer Roadmap)",
            },
            {
                "id": "zsjvFFKOm3c",
                "label": "Part 2: Practice Examples (SQL Explained in 100 Seconds)",
            },
            {"id": "yMqldbY2AAg", "label": "Part 3: Test (Roadmap for Learning SQL)"},
        ],
        "notes_bullets": [
            "Model data with relational tables.",
            "Implement CRUD with safe query patterns.",
            "Connect backend logic to database operations.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "world-geography-cultures": {
        "id": "world-geography-cultures",
        "title": "World Geography & Cultures",
        "level_label": "Middle School",
        "subject_label": "Social Studies & History",
        "description": "Explore physical maps, climate zones, population distribution, and diverse cultural heritage worldwide.",
        "videos": [
            {
                "id": "hNVD8fyIsEI",
                "label": "Part 1: Introduction (World Geography Made Easy)",
            },
            {
                "id": "AehgK6e_a5Y",
                "label": "Part 2: Practice Examples (7 Continents of the World Overview)",
            },
            {
                "id": "zZJFozFsnIU",
                "label": "Part 3: Test (A Geopolitical Tour of the World)",
            },
        ],
        "notes_bullets": [
            "Recognize climate zones and their features.",
            "Describe how geography influences culture.",
            "Practice reading maps for key information.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "modern-world-history": {
        "id": "modern-world-history",
        "title": "Modern World History",
        "level_label": "High School • G10",
        "subject_label": "Social Studies & History",
        "description": "Examine the Industrial Revolution, World Wars, Cold War dynamics, and globalization in the 20th century.",
        "videos": [
            {
                "id": "w3572wc-D28",
                "label": "Part 1: Introduction (AP World History in 18 Minutes)",
            },
            {
                "id": "TZ956rJDpsg",
                "label": "Part 2: Practice Examples (Key Time Periods for AP World History: Modern)",
            },
            {"id": "HYmYrFFWffw", "label": "Part 3: Test (2026 AP World Full Review)"},
        ],
        "notes_bullets": [
            "Use timelines to connect causes and effects.",
            "Compare major world events by era.",
            "Summarize key outcomes and their impacts.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "sociology-social-structures": {
        "id": "sociology-social-structures",
        "title": "Sociology & Social Structures",
        "level_label": "High School • G11",
        "subject_label": "Social Studies & History",
        "description": "Study social interactions, structural institutions, cultural diversities, and behavioral control elements within communities.",
        "videos": [
            {
                "id": "3552UIEdAjs",
                "label": "Part 1: Introduction (Social Structures: Definition & Examples)",
            },
            {
                "id": "m4abN2cfNO8",
                "label": "Part 2: Practice Examples (What are Social Institutions?)",
            },
            {
                "id": "9KR1bad76qg",
                "label": "Part 3: Test (Social institutions | Society and Culture)",
            },
        ],
        "notes_bullets": [
            "Identify key institutions in society.",
            "Explain how culture and norms influence behavior.",
            "Analyze social change with examples.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
    "macroeconomics-principles": {
        "id": "macroeconomics-principles",
        "title": "Macroeconomics Principles",
        "level_label": "High School • G12",
        "subject_label": "Social Studies & History",
        "description": "Understand national income, inflation, monetary/fiscal policies, and international trade models.",
        "videos": [
            {
                "id": "MKO1icFVtDc",
                "label": "Part 1: Introduction (Macroeconomics- Everything You Need to Know)",
            },
            {
                "id": "d8uTB5XorBw",
                "label": "Part 2: Practice Examples (Macroeconomics: Crash Course Economics)",
            },
            {"id": "xmdBlkrkTN4", "label": "Part 3: Test (Macroeconomics Made Simple)"},
        ],
        "notes_bullets": [
            "Explain the basics of inflation and employment.",
            "Compare fiscal vs monetary policy goals.",
            "Understand trade models and key indicators.",
        ],
        "resources": [
            {"type": "video", "label": "Video", "icon": "bi bi-play-btn-fill"},
            {
                "type": "pdf",
                "label": "Basic Algebra Worksheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-worksheet.pdf",
            },
            {
                "type": "pdf",
                "label": "Algebra Cheat Sheet",
                "icon": "bi bi-file-pdf-fill",
                "pdf_url": "https://example.com/algebra-cheat-sheet.pdf",
            },
            {"type": "notes", "label": "Notes", "icon": "bi bi-journal-text"},
        ],
    },
}
