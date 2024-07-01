from app import db, Quiz, Question, app

quizzes = [
    {
        "title": "AI Development in Python",
        "description": "Questions about developing AI using Python.",
        "questions": [
            {
                "question_text": "Which library is most commonly used for AI development in Python?",
                "option1": "NumPy",
                "option2": "TensorFlow",
                "option3": "Pandas",
                "option4": "SciPy",
                "correct_option": "TensorFlow",
                
            },
            {
                "question_text": "What is deep learning?",
                "option1": "A subset of machine learning",
                "option2": "A type of hardware",
                "option3": "A programming language",
                "option4": "A data storage method",
                "correct_option": "A subset of machine learning",
                
            },
            {
                "question_text": "Which library is used to create neural network models in Python?",
                "option1": "Keras",
                "option2": "BeautifulSoup",
                "option3": "Flask",
                "option4": "Requests",
                "correct_option": "Keras",
                
            },
            {
                "question_text": "How many types of artificial neural networks are there?",
                "option1": "1",
                "option2": "2",
                "option3": "3",
                "option4": "4",
                "correct_option": "3",
                
            },
            {
                "question_text": "Which library is used for data analysis in Python?",
                "option1": "NumPy",
                "option2": "TensorFlow",
                "option3": "Pandas",
                "option4": "SciPy",
                "correct_option": "Pandas",
                
            },
            {
                "question_text": "What is a popular library used in AI projects in Python?",
                "option1": "PyTorch",
                "option2": "Django",
                "option3": "Flask",
                "option4": "Requests",
                "correct_option": "PyTorch",
                
            }
        ]
    },
    {
        "title": "Computer Vision",
        "description": "Questions about computer vision.",
        "questions": [
            {
                "question_text": "What is computer vision?",
                "option1": "A field of AI that enables computers to interpret and process digital images and videos",
                "option2": "A type of computer hardware",
                "option3": "A new programming language",
                "option4": "A method for storing data",
                "correct_option": "A field of AI that enables computers to interpret and process digital images and videos",
                
            },
            {
                "question_text": "Which library is used for computer vision in Python?",
                "option1": "OpenCV",
                "option2": "TensorFlow",
                "option3": "Scikit-learn",
                "option4": "Matplotlib",
                "correct_option": "OpenCV",
                
            },
            {
                "question_text": "What is image classification?",
                "option1": "The process of assigning a label to an image based on its content",
                "option2": "The process of compressing an image",
                "option3": "The process of enhancing an image",
                "option4": "The process of storing an image",
                "correct_option": "The process of assigning a label to an image based on its content",
                
            },
            {
                "question_text": "What is a popular library for image processing in Python?",
                "option1": "OpenCV",
                "option2": "Pandas",
                "option3": "NumPy",
                "option4": "TensorFlow",
                "correct_option": "OpenCV",
                
            },
            {
                "question_text": "Which library is used for face recognition in Python?",
                "option1": "Face_recognition",
                "option2": "Requests",
                "option3": "BeautifulSoup",
                "option4": "Flask",
                "correct_option": "Face_recognition",
                
            },
            {
                "question_text": "Which language is the OpenCV library written in?",
                "option1": "C",
                "option2": "C++",
                "option3": "Python",
                "option4": "Java",
                "correct_option": "C++",
                
            }
        ]
    },
    {
        "title": "NLP (Natural Language Processing)",
        "description": "Questions about NLP (Natural Language Processing).",
        "questions": [
            {
                "question_text": "What is NLP?",
                "option1": "A field of AI that focuses on the interaction between computers and human language",
                "option2": "A type of hardware",
                "option3": "A programming language",
                "option4": "A data storage method",
                "correct_option": "A field of AI that focuses on the interaction between computers and human language",
                
            },
            {
                "question_text": "Which library is used for NLP in Python?",
                "option1": "NLTK",
                "option2": "NumPy",
                "option3": "SciPy",
                "option4": "Matplotlib",
                "correct_option": "NLTK",
                
            },
            {
                "question_text": "Which library is used for text mining in Python?",
                "option1": "BeautifulSoup",
                "option2": "Requests",
                "option3": "spaCy",
                "option4": "TensorFlow",
                "correct_option": "spaCy",
                
            },
            {
                "question_text": "Which language do NLP models process?",
                "option1": "Natural language",
                "option2": "Machine language",
                "option3": "Programming language",
                "option4": "Artificial language",
                "correct_option": "Natural language",
                
            },
            {
                "question_text": "What is text preprocessing?",
                "option1": "The process of cleaning and normalizing text data",
                "option2": "The process of translating text",
                "option3": "The process of storing text",
                "option4": "The process of compressing text",
                "correct_option": "The process of cleaning and normalizing text data",
                
            },
            {
                "question_text": "Which library is used for processing text data in Python?",
                "option1": "Pandas",
                "option2": "NumPy",
                "option3": "NLTK",
                "option4": "Matplotlib",
                "correct_option": "NLTK",
                
            }
        ]
    },
    {
        "title": "Implementing AI Models in Python Applications",
        "description": "Questions about implementing AI models in Python applications.",
        "questions": [
            {
                "question_text": "How do you implement an AI model in Python?",
                "option1": "Using an appropriate library like TensorFlow or Keras",
                "option2": "Using a database",
                "option3": "Using a programming language",
                "option4": "Using a web framework",
                "correct_option": "Using an appropriate library like TensorFlow or Keras",
                
            },
            {
                "question_text": "What is Flask?",
                "option1": "Python web framework",
                "option2": "Python library",
                "option3": "Database",
                "option4": "Python module",
                "correct_option": "Python web framework",
                
            },
            {
                "question_text": "Which library is used for AI models in Python?",
                "option1": "TensorFlow",
                "option2": "Requests",
                "option3": "BeautifulSoup",
                "option4": "Flask",
                "correct_option": "TensorFlow",
                
            },
            {
                "question_text": "How do you deploy an AI model in a web application?",
                "option1": "Using frameworks like Flask or Django",
                "option2": "Using a database",
                "option3": "Using a programming language",
                "option4": "Using a text editor",
                "correct_option": "Using frameworks like Flask or Django",
                
            },
            {
                "question_text": "Which library is used to create APIs in Python?",
                "option1": "Flask",
                "option2": "Requests",
                "option3": "BeautifulSoup",
                "option4": "NumPy",
                "correct_option": "Flask",
                
            },
            {
                "question_text": "How is the performance of AI models evaluated?",
                "option1": "Using metrics like accuracy, precision, recall, and F1 score",
                "option2": "Using a database",
                "option3": "Using a programming language",
                "option4": "Using a text editor",
                "correct_option": "Using metrics like accuracy, precision, recall, and F1 score",
                
            }
        ]
    }
]

with app.app_context():
    for quiz_data in quizzes:
        quiz = Quiz(title=quiz_data["title"], description=quiz_data["description"])
        db.session.add(quiz)
        db.session.commit()

        for question_data in quiz_data["questions"]:
            question = Question(
                question_text=question_data["question_text"],
                option1=question_data.get("option1"),
                option2=question_data.get("option2"),
                option3=question_data.get("option3"),
                option4=question_data.get("option4"),
                correct_option=question_data["correct_option"],
                quiz_id=quiz.id
            )
            db.session.add(question)
        db.session.commit()
