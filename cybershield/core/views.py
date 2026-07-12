from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib.auth.models import User

# Complete Multilingual Question Bank partitioned by Level
QUESTION_BANK = {
    'English': {
        'Beginner': [
        {
            'step': '1/4',
            'type': 'alphabet_sequence',
            'question': 'Which letter comes right after "M"?',
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%23a5f3fc"/><stop offset="40%" stop-color="%2338bdf8"/><stop offset="70%" stop-color="%23a855f7"/><stop offset="100%" stop-color="%23d946ef"/></linearGradient></defs><rect width="100%" height="100%" fill="url(%23g)"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="120" font-weight="bold" fill="white" text-anchor="middle" letter-spacing="15">M _</text></svg>',
            'options': ['L', 'N', 'O', 'P'],
            'correct': 'N'
        },
        {
            'step': '2/4',
            'type': 'spelling_check',
            'question': 'Fill in the missing letter to name this animal: C _ T',
            'image_url': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&q=80',  # Cat
            'options': ['A', 'O', 'E', 'U'],
            'correct': 'A'
        },
        {
            'step': '3/4',
            'type': 'object_match',
            'question': 'Look at the image below. Select the correct word matching it:',
            'image_url': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=500&q=80',  # Apple
            'options': ['Ball', 'Apple', 'Tree', 'Book'],
            'correct': 'Apple'
        },
        {
            'step': '4/4',
            'type': 'basic_vowel_check',
            'question': 'Identify the word that starts with a vowel sound:',
            'image_url': 'https://placehold.co/500x300/4f46e5/ffffff?text=Vowels:+A,+E,+I,+O,+U',
            'options': ['Dog', 'Elephant', 'Cat', 'Fish'],
            'correct': 'Elephant'
        }
    ],
    'Intermediate': [
        {
            'step': '1/4',
            'type': 'grammar_tense',
            'question': 'Identify the correct sentence structure:',
            'image_url': 'https://placehold.co/500x300/0ea5e9/ffffff?text=Grammar+Tense+Quiz',
            'options': ['He go to school yesterday.', 'He went to school yesterday.', 'He going to school yesterday.', 'He gone to school yesterday.'],
            'correct': 'He went to school yesterday.'
        },
        {
            'step': '2/4',
            'type': 'vocabulary_synonym',
            'question': 'What is the closest meaning (synonym) of the word "Huge"?',
            'image_url': 'https://placehold.co/500x300/10b981/ffffff?text=Vocabulary:+Huge',
            'options': ['Small', 'Tiny', 'Large', 'Weak'],
            'correct': 'Large'
        },
        {
            'step': '3/4',
            'type': 'sentence_completion',
            'question': 'Complete the phrase: "She is interested _______ learning new languages."',
            'image_url': 'https://placehold.co/500x300/f59e0b/ffffff?text=Fill+in+the+Blank',
            'options': ['on', 'at', 'in', 'for'],
            'correct': 'in'
        },
        {
            'step': '4/4',
            'type': 'conjunction_link',
            'question': 'Choose the right conjunction: "I wanted to go out, _______ it was raining heavily."',
            'image_url': 'https://placehold.co/500x300/ef4444/ffffff?text=Conjunctions',
            'options': ['so', 'but', 'because', 'or'],
            'correct': 'but'
        }
    ],
    'Advanced': [
        {
            'step': '1/4',
            'type': 'idiom_comprehension',
            'question': 'What does the idiom "Spill the beans" mean?',
            'image_url': 'https://placehold.co/500x300/8b5cf6/ffffff?text=Idioms:+Spill+the+Beans',
            'options': ['To cook food', 'To reveal a secret accidentally', 'To drop vegetables', 'To clean the kitchen'],
            'correct': 'To reveal a secret accidentally'
        },
        {
            'step': '2/4',
            'type': 'complex_comprehension',
            'question': 'Identify the sentence containing an active voice layout error:',
            'image_url': 'https://placehold.co/500x300/ec4899/ffffff?text=Comprehension+Challenge',
            'options': ['The chef prepared a delicious meal.', 'The book was read by Sarah in one sitting.', 'Mistakes were made by the management system.', 'The dog barked at the stranger loudly.'],
            'correct': 'Mistakes were made by the management system.'
        },
        {
            'step': '3/4',
            'type': 'context_cloze',
            'question': 'Select the most appropriate word: "The company dynamic policy changes had a _______ effect on employee morale."',
            'image_url': 'https://placehold.co/500x300/6366f1/ffffff?text=Context+Cloze',
            'options': ['negligent', 'profound', 'profuse', 'procrastinated'],
            'correct': 'profound'
        },
        {
            'step': '4/4',
            'type': 'rhetorical_device',
            'question': 'Identify the figure of speech used here: "The stars danced playfully in the moonlit sky."',
            'image_url': 'https://placehold.co/500x300/14b8a6/ffffff?text=Figures+of+Speech',
            'options': ['Metaphor', 'Simile', 'Personification', 'Hyperbole'],
            'correct': 'Personification'
        }
    ]
    },
    'Telugu': {
        'Beginner': [
        {
            'step': '1/4',
            'type': 'alphabet_sequence',
            'question': '‘అ’ అక్షరం తర్వాత వచ్చే సరైన అక్షరాన్ని గుర్తించండి:',
            'image_url': 'https://placehold.co/500x300/4f46e5/ffffff?text=Telugu+Alphabet',
            'options': ['ఇ', 'ఆ', 'ఉ', 'ఋ'],
            'correct': 'ఆ'
        },
        {
            'step': '2/4',
            'type': 'spelling_check',
            'question': 'కింది ఖాళీని పూరించి సరైన పదాన్ని తయారుచేయండి: _లం',
            'image_url': 'https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=500&q=80',  # Pen
            'options': ['మ', 'క', 'ప', 'ర'],
            'correct': 'క'
        },
        {
            'step': '3/4',
            'type': 'object_match',
            'question': 'చిత్రాన్ని చూసి సరైన పదాన్ని ఎంచుకోండి (🌳):',
            'image_url': 'https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=500&q=80',  # Tree
            'options': ['ఆకు', 'చెట్టు', 'పువ్వు', 'కాయ'],
            'correct': 'చెట్టు'
        },
        {
            'step': '4/4',
            'type': 'vowel_identification',
            'question': 'కింది అక్షరాలలో "అచ్చు" (Vowel) అక్షరాన్ని గుర్తించండి:',
            'image_url': 'https://placehold.co/500x300/0ea5e9/ffffff?text=Telugu+Vowels',
            'options': ['క', 'చ', 'ఇ', 'త'],
            'correct': 'ఇ'
        }
    ],
    'Intermediate': [
        {
            'step': '1/4',
            'type': 'grammar_tense',
            'question': '"రాము నిన్న ఊరికి వెళ్ళాడు" - ఇది ఏ కాలానికి చెందిన వాక్యం?',
            'image_url': 'https://placehold.co/500x300/10b981/ffffff?text=Telugu+Grammar',
            'options': ['భవిష్యత్ కాలం', 'వర్తమాన కాలం', 'భూత కాలం', 'ఏదీ కాదు'],
            'correct': 'భూత కాలం'
        },
        {
            'step': '2/4',
            'type': 'vocabulary_synonym',
            'question': '‘సూర్యుడు’ అనే పదానికి సమానార్థక పదం (పర్యాయపదం) ఏమిటి?',
            'image_url': 'https://images.unsplash.com/photo-1538370965046-79c0d6907d47?w=500&q=80',  # Sun
            'options': ['చంద్రుడు', 'భానుడు', 'నక్షత్రం', 'ఆకాశం'],
            'correct': 'భానుడు'
        },
        {
            'step': '3/4',
            'type': 'sentence_completion',
            'question': 'వాక్యాన్ని పూర్తి చేయండి: "ఆమె ఎంతో _______ సంగీతం పాడుతుంది."',
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">వాక్య పూరణ</text></svg>',
            'options': ['కోపంగా', 'మధురంగా', 'వేగంగా', 'పెద్దగా'],
            'correct': 'మధురంగా'
        },
        {
            'step': '4/4',
            'type': 'plural_check',
            'question': '‘పుస్తకం’ అనే పదానికి సరైన బహువచన రూపం ఏది?',
            'image_url': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=500&q=80',  # Books
            'options': ['పుస్తకాలు', 'పుస్తకములు', 'పుస్తక', 'పుస్తకా'],
            'correct': 'పుస్తకాలు'
        }
    ],
    'Advanced': [
        {
            'step': '1/4',
            'type': 'idiom_comprehension',
            'question': '‘తామరతంపర’ అనే జాతీయం ఏ సందర్భంలో ఉపయోగిస్తారు?',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "జాతీయాలు" అని తెలుగులో వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">జాతీయాలు</text></svg>',
            'options': ['తక్కువగా ఉండటం', 'మితిమీరి అభివృద్ధి చెందడం', 'నాశనమవ్వడం', 'ఆలస్యం కావడం'],
            'correct': 'మితిమీరి అభివృద్ధి చెందడం'
        },
        {
            'step': '2/4',
            'type': 'complex_comprehension',
            'question': 'కింది వాటిలో సరైన ‘సంధి’ విభజన రూపం ఏది?',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "సంధి" అని తెలుగులో వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">సంధి</text></svg>',
            'options': ['రాముడు + అతడు = రాముడతడు ', 'రామ + అతడు = రాముడు', 'రాము + అతడు = రాముడతడు', 'రాముడు + తడు = రాముడతడు'],
            'correct': 'రాము + అతడు = రాముడతడు'
        },
        {
            
                'step': '3/4',
                'type': 'context_cloze',
                'question': '"దేశాభివృద్ధికి ప్రతి ఒక్కరూ తమ వంతు _______ అందించాలి."',
                # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "సందర్భోచిత పూరణ" అని తెలుగులో వచ్చే పర్మనెంట్ SVG కోడ్
                'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">సందర్భోచిత పూరణ</text></svg>',
                'options': ['నిరాశ', 'నష్టం', 'సహకారం', 'వ్యతిరేకత'],
                'correct': 'సహకారం'
            

        },
        {
            'step': '4/4',
            'type': 'proverb_check',
            'question': '‘అరచేతిలో వైకుంఠం చూపించడం’ అనే సామెతకు సరైన అర్థం ఏమిటి?',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "సామెతలు" అని తెలుగులో వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">సామెతలు</text></svg>',
            'options': ['నిజం చెప్పడం', 'అసాధ్యమైన వాటిని సాధ్యమైనట్లు నమ్మించడం', 'సహాయం చేయడం', 'దేవుడిని చూపించడం'],
            'correct': 'అసాధ్యమైన వాటిని సాధ్యమైనట్లు నమ్మించడం'
        }
    ]
    },
    'Hindi': {
        'Beginner': [
        
            {
            'step': '1/4',
            'type': 'alphabet_sequence',
            'question': 'वर्णमाला में "अ" के तुरंत बाद कौन सा अक्षर आता है?',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "वर्णमाला" (Vowels/Alphabet) అని వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">वर्णमाला</text></svg>',
            'options': ['इ', 'आ', 'उ', 'ए'],
            'correct': 'आ'
        },
        {
            'step': '2/4',
            'type': 'spelling_check',
            'question': 'इस शब्द को पूरा करने के लिए सही अक्षर चुनें: क _ ल',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "शब्द पूरा करें" (Spelling Check) అని వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">शब्द पूरा करें</text></svg>',
            'options': ['म', 'र', 'न', 'स'],
            'correct': 'म'
        },
        {
            'step': '3/4',
            'type': 'object_match',
            'question': 'चित्र देखकर सही शब्द का चयन करें (🏡):',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "चित्र पहचानिए" (Object Match) అని వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">चित्र पहचानिए</text></svg>',
            'options': ['पानी', 'घर', 'पेड़', 'किताब'],
            'correct': 'घर'
        },
        {
            'step': '4/4',
            'type': 'number_check',
            'question': 'संख्या "४" को शब्दों में what written?',
            # ఆరెంజ్ బ్యాక్‌గ్రౌండ్ పైన "संख्या ज्ञान" (Numbers) అని వచ్చే పర్మనెంట్ SVG కోడ్
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">संख्या ज्ञान</text></svg>',
            'options': ['दो', 'तीन', 'चार', 'पाँच'],
            'correct': 'चार'
        }
    ],
    'Intermediate': [
        {
            'step': '1/4',
            'type': 'grammar_tense',
            'question': '"वह कल दिल्ली जाएगा।" यह वाक्य किस काल का है?',
            # आरेंज बैकग्राउंड के साथ "काल ज्ञान" (Tense) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">काल ज्ञान</text></svg>',
            'options': ['भूतकाल', 'वर्तमान काल', 'भविष्य काल', 'अपूर्ण भूतकाल'],
            'correct': 'भविष्य काल'
        },
        {
            'step': '2/4',
            'type': 'vocabulary_synonym',
            'question': '"आकाश" शब्द का सही पर्यायवाची शब्द क्या है?',
            # आरेंज बैकग्राउंड के साथ "पर्यायवाची शब्द" (Synonyms) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">पर्यायवाची शब्द</text></svg>',
            'options': ['पाताल', 'गगन', 'धरती', 'समुद्र'],
            'correct': 'गगन'
        },
        {
            'step': '3/4',
            'type': 'sentence_completion',
            'question': 'वाक्य पूरा करें: "हवा बहुत _______ चल रही है।"',
            # आरेंज बैकग्राउंड के साथ "वाक्य पूरण" (Sentence Completion) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">वाक्य पूरण</text></svg>',
            'options': ['मीठी', 'ठंडी', 'कड़वी', 'भारी'],
            'correct': 'ठंडी'
        },
        {
            'step': '4/4',
            'type': 'gender_check',
            'question': '"किताब" शब्द का सही लिंग क्या है?',
            # आरेंज बैकग्राउंड के साथ "लिंग निर्णय" (Gender Check) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">लिंग निर्णय</text></svg>',
            'options': ['पुल्लिंग', 'स्त्रीलिंग', 'उभयलिंग', 'कोई नहीं'],
            'correct': 'स्त्रीलिंग'
        }
    ],
    'Advanced': [
        {
            'step': '1/4',
            'type': 'idiom_comprehension',
            'question': '"अंगूठा दिखाना" इस मुहावरे का सही अर्थ क्या है?',
            # आरेंज बैकग्राउंड के साथ "मुहावरे" (Idioms) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">मुहावरे</text></svg>',
            'options': ['मदद करने से साफ़ मना करना', 'दोस्ती करना', 'चिढ़ाना', 'जीत की घोषणा करना'],
            'correct': 'मदद करने से साफ़ मना करना'
        },
        {
            'step': '2/4',
            'type': 'complex_comprehension',
            'question': 'निम्नलिखित में से शुद्ध वाक्य का चयन कीजिए:',
            # आरेंज बैकग्राउंड के साथ "वाक्य शुद्धि" (Sentence Correction) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">वाक्य शुद्धि</text></svg>',
            'options': ['मेरे को घर जाना है।', 'मुझे घर जाना है।', 'मैं घर को जाना है।', 'मुझको घर को जाना है।'],
            'correct': 'मुझे घर जाना है।'
        },
        {
            'step': '3/4',
            'type': 'context_cloze',
            'question': '"वैज्ञानिकों ने कठिन परिश्रम के बाद नई दवा का _______ किया।"',
            # आरेंज बैकग्राउंड के साथ "रिक्त स्थान" (Context Cloze) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">रिक्त स्थान</text></svg>',
            'options': ['आविष्कार', 'अनुवाद', 'विनाश', 'प्रचार'],
            'correct': 'आविष्कार'
        },
        {
            'step': '4/4',
            'type': 'sandhi_check',
            'question': '"सूर्योदय" शब्द का सही संधि-विच्छेद क्या होगा?',
            # आरेंज बैकग्राउंड के साथ "संधि विच्छेद" (Sandhi Check) SVG कोड
            'image_url': 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500"><rect width="100%" height="100%" fill="%23e68a00"/><text x="50%" y="55%" font-family="system-ui, -apple-system, sans-serif" font-size="65" font-weight="bold" fill="white" text-anchor="middle">संधि विच्छेद</text></svg>',
            'options': ['सूर्य + उदय', 'सूर्यो + दय', 'सूर्य + दय', 'सूर्या + उदय'],
            'correct': 'सूर्य + उदय'
        }
    ]
}
}
# Dynamic Interface Translations
UI_TRANSLATIONS = {
    'English': {
        'step3_title': 'Choose your expertise level',
        'opt_beginner': 'Beginner (Starting Fresh)',
        'opt_advanced': 'Advanced (Solid Experience)',
        'opt_expert': 'Expert (Master Level)',
        'step4_title': 'How did you hear about us?',
        'src_friend': 'Friend / Family',
        'src_social': 'Social Media',
        'src_search': 'Online Search',
        'quiz_submit': 'Submit Answer',
        'results_title': 'Great Job',
        'results_desc': 'You have completed your personalized assessment.',
        'accuracy': 'Accuracy',
        'dashboard_btn': 'Go to Dashboard',
        'btn_retake': 'Retake Assessment',
    },
    'Telugu': {
        'step3_title': 'మీ నైపుణ్య స్థాయిని ఎంచుకోండి',
        'opt_beginner': 'బిగినర్స్ (ప్రారంభకులు)',
        'opt_advanced': 'ఇంటర్మీడియట్ (మధ్యస్థం)',
        'opt_expert': 'ఎక్స్‌పర్ట్ (మాస్టర్ లెవెల్)',
        'step4_title': 'మా గురించి మీకు ఎలా తెలిసింది?',
        'src_friend': 'స్నేహితులు / కుటుంబం',
        'src_social': 'సోషల్ మీడియా',
        'src_search': 'ఆన్‌లైన్ సెర్చ్',
        'quiz_submit': 'సమాధానాన్ని సమర్పించండి',
        'results_title': 'అద్భుతమైన పని',
        'results_desc': 'మీరు మీ వ్యక్తిగతీకరించిన విశ్లేషణ మూల్యాంకనాన్ని పూర్తి చేసారు.',
        'accuracy': 'ఖచ్చితత్వం',
        'dashboard_btn': 'డ్యాష్‌బోర్డ్‌కి వెళ్లండి',
        'btn_retake': 'మళ్ళీ పరీక్ష రాయండి',
    },
    'Hindi': {
        'step3_title': 'अपना विशेषज्ञता स्तर चुनें',
        'opt_beginner': 'शुरुआती (Beginner)',
        'opt_advanced': 'मध्यम (Intermediate)',
        'opt_expert': 'विशेषज्ञ (Expert)',
        'step4_title': 'आपको हमारे बारे में कैसे पता चला?',
        'src_friend': 'मित्र / परिवार',
        'src_social': 'सोशल मीडिया',
        'src_search': 'ऑनलाइन खोज',
        'quiz_submit': 'उत्तर जमा करें',
        'results_title': 'बहुत बढ़िया',
        'results_desc': 'आपने अपना व्यक्तिगत मूल्यांकन पूरा कर लिया है।',
        'accuracy': 'सटीकता',
        'dashboard_btn': 'डैशबोर्ड पर जाएं',
        'btn_retake': 'पुनर्मूल्यांकन करें',
    }
}

def auth_entry_view(request):
    error_msg = None
    form_type = request.GET.get('action', 'register')

    if request.method == 'POST':
        action_type = request.POST.get('action_type')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if action_type == 'register':
            email = request.POST.get('email')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                error_msg = "Passwords do not match!"
            elif User.objects.filter(username=username).exists():
                error_msg = "Username already taken."
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth_login(request, user)
                
                request.session['onboarding_step'] = 2
                request.session['learner_name'] = username
                request.session['answers'] = {}
                request.session['quiz_step'] = 0
                request.session['selected_language'] = "English"
                request.session['skill_level'] = "Beginner"
                request.session.modified = True
                return redirect('assessment')

        elif action_type == 'login':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                
                request.session['onboarding_step'] = 2
                request.session['learner_name'] = username
                request.session['answers'] = {}
                request.session['quiz_step'] = 0
                request.session['selected_language'] = "English"
                request.session['skill_level'] = "Beginner"
                request.session.modified = True
                return redirect('assessment')
            else:
                error_msg = "Invalid credentials."
                form_type = 'login'

    return render(request, 'core/auth.html', {'error': error_msg, 'form_type': form_type})


def assessment_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_entry')

    onboarding_step = request.session.get('onboarding_step', 2)
    quiz_step = request.session.get('quiz_step', 0)
    answers = request.session.get('answers', {})
    lang = request.session.get('selected_language', 'English')
    skill = request.session.get('skill_level', 'Beginner')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'start_over':
            request.session['onboarding_step'] = 2
            request.session['quiz_step'] = 0
            request.session['answers'] = {}
            request.session.modified = True
            return redirect('assessment')

        elif onboarding_step == 2:
            request.session['selected_language'] = request.POST.get('language', 'English')
            request.session['onboarding_step'] = 3
            request.session.modified = True
            return redirect('assessment')

        elif onboarding_step == 3:
            # Map input option value to our bank levels (Beginner, Intermediate, Advanced)
            posted_skill = request.POST.get('skill_level', 'Beginner')
            if 'Advanced' in posted_skill or 'Intermediate' in posted_skill:
                skill_mapped = 'Intermediate'
            elif 'Expert' in posted_skill or 'Advanced' in posted_skill:
                skill_mapped = 'Advanced'
            else:
                skill_mapped = 'Beginner'
                
            request.session['skill_level'] = skill_mapped
            request.session['onboarding_step'] = 4
            request.session.modified = True
            return redirect('assessment')

        elif onboarding_step == 4:
            request.session['hear_about'] = request.POST.get('hear_about', 'Friend')
            request.session['onboarding_step'] = 5
            request.session['quiz_step'] = 0
            request.session.modified = True
            return redirect('assessment')

        elif onboarding_step == 5:
            selected_option = request.POST.get('selected_option')
            if selected_option:
                answers[str(quiz_step)] = selected_option
                request.session['answers'] = answers
                request.session['quiz_step'] = quiz_step + 1
                request.session.modified = True
            return redirect('assessment')

    # Safely fetch questions using structured dictionary keys
    lang_bank = QUESTION_BANK.get(lang, QUESTION_BANK['English'])
    current_questions = lang_bank.get(skill, lang_bank['Beginner'])

    if onboarding_step == 5 and quiz_step >= len(current_questions):
        score = sum(1 for idx, q in enumerate(current_questions) if answers.get(str(idx)) == q['correct'])
        return render(request, 'core/assessment.html', {
            'completed': True, 
            'score': score, 
            'total': len(current_questions),
            'percentage': int((score / len(current_questions)) * 100) if current_questions else 0,
            'learner_name': request.session.get('learner_name', 'Explorer'),
            'selected_language': lang, 
            'skill_level': skill,
            'ui': UI_TRANSLATIONS.get(lang, UI_TRANSLATIONS['English'])
        })

    return render(request, 'core/assessment.html', {
        'completed': False, 
        'onboarding_step': onboarding_step, 
        'quiz_step_number': quiz_step + 1,
        'total_questions': len(current_questions),
        'question': current_questions[quiz_step] if onboarding_step == 5 and quiz_step < len(current_questions) else None,
        'progress_percent': int((quiz_step / len(current_questions)) * 100) if onboarding_step == 5 and current_questions else 0,
        'learner_name': request.session.get('learner_name', 'Explorer'),
        'ui': UI_TRANSLATIONS.get(lang, UI_TRANSLATIONS['English'])
    })

def home_view(request):
    return render(request, 'core/home.html')

def logout_view(request):
    logout(request)
    return redirect('auth_entry')
