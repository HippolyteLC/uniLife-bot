from typing import List, Dict

# keywords_studying: List[str] = ["assignment", "task"]
# keywords_sport: List[str] = ["sport", "football", "basketball", "sport opportunities", "team", "game"]

keywords_studying: List[str] = ["textbooks", "notebooks", "paper", "pens", "pencils", "highlighters", 
    "desk", "chair", "organizational", "laptop", "internet", "charging", 
    "planner", "timer", "mind", "maps", "summarization", "note", 
    "online", "databases", "library", "reference", "break", "practice", "mock", 
    "language", "study", "educational", "grammar", "thesaurus", "writing", "motivational", "visual", 
    "comfortable", "extra", "external", "whiteboard", "markers", "index", "first", "emergency",
    "studying", "student", "studies", "students", "learn", "material", "assigment", "task", "study group"
    "counseling", "essay", "examination", "stressed", "anxious", "credits", "course", "courses", "period",
    "semester", "report"]

keywords_sport: List[str] = ["sport", "football", "basketball", "sport opportunities", "team", "athlete", "physical", "training",
    "soccer", "tennis", "korfball", "waterpolo", "swimming", "running", "lifting", "weight", "gym", "rugby", "sailing", "hockey",
    "rowing", "racing", "formula 1", "baseball", "softball", "handball", "boxing", "golf", "american football", "cricket",
    "skiing", "teammate", "fighting", "self-defense", "karate", "martial art", "yudo", "zumbda", "yoga", "aikido"]

keywords_social_activities: List[str] = ["social", "social activities", "student association", "events",
                                         "upcoming events", "upcoming social events", "social events"]

sport_keywords: Dict[str, List[str]] = {
    "aikido": ["martial arts", "combat", "self-defense"],
    "basketball": ["team", "ball", "score", "court"],
    "tennis": ["ball", "racket", "court", "sets"],
    "swimming": ["water", "physical", "exercise"],
    "football": ["team", "ball", "score", "field", "goal"],
    "zumba": ["dance", "physical", "exercise", "rhythm"],
    "karate": ["martial arts", "combat", "self-defense"],
    "yoga": ["spiritual", "relax", "stretch", "pose", "breathe"],
    "waterpolo": ["water", "physical", "exercise", "ball", "team"]
}
association_keywords: Dict[str, List[str]] = {
    "Poetry Pals": ["lorem ipsum"],
    "Debate Club": ["lorem ipsum"],
    "Science Society": ["lorem ipsum"],
    "Painting and Pottery": ["lorem ipsum"],
    "Language Club": ["lorem ipsum"],
    "International Students Society": ["lorem ipsum"],
    "Students for Sustainability": ["lorem ipsum"],
    "Animal Shelter Volunteers": ["animals", "help", "volounteering"],
    "Bunch of Backpackers": ["lorem ipsum"]
}

redundant_words: List[str] = ["the", "and", "why", "what", "where", "who", "when", "how", "because", "if", "this",
                              "that", "there",
                              "than", "then", "however", "maybe", "some", "to", "from", "back", "more", "less",
                              "better", "worse",
                              "else", "please", "help"]
