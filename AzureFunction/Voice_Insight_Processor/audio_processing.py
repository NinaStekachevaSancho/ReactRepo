from Voice_Insight_Processor.WhisperAudioProcessor import completion

def get_leanguege(transcription):
    system = {"role":"system", "content":"Detect what language is the input"}
    messages = [system,
                {"role":"user","content":"Mi reciente viaje a Roma fue bastante decepcionante. La ciudad estaba superpoblada, lo que dificultó disfrutar de sitios famosos como el Coliseo y la Fuente de Trevi. A pesar de su importancia histórica, el encanto de la ciudad quedó ensombrecido por la abrumadora cantidad de turistas. Además, encontré que los restaurantes locales eran caros y la calidad de la comida decepcionante. Navegar por la ciudad también fue un problema debido al confuso transporte público y las calles congestionadas. Esperaba una experiencia más auténtica, pero desafortunadamente, se sintió demasiado comercializada y turística para mi gusto."},
                {"role":"assistant","content":"Spanish"},
                {"role":"user","content":"Fy mhrofiad diweddar gyda'r smartwatch newydd o gwmni XYZ oedd yn aruthrol. Roedd y dyluniad yn fodern ac yn chwaethus, a'r swyddogaethau monitro iechyd yn fanwl a chywir. Roedd gallu olrhain fy ymarfer corff a monitro cwsg yn hynod o ddefnyddiol. Roedd y bywyd batri yn wych hefyd, gan bara dyddiau heb angen ailwefru. Fodd bynnag, roedd y rhyngwyneb defnyddiwr braidd yn gymhleth i'w defnyddio ar y dechrau. Serch hynny, ar ôl ychydig o ddefnydd, daeth yn haws. Yn gyffredinol, roedd y smartwatch yn cyflawni fy anghenion yn berffaith."},
                {"role":"assistant","content":"Welsh"},
                {"role":"user","content": transcription}
                ]
    return completion(messages)

def get_translation(transcription, leanguege):
    system = {"role":"system", "content":"Translate the input text from the given lengueage to English."}
    messages = [system,
                {"role":"user","content":f"Tanslate from Spanish to English: Mi reciente viaje a Roma fue bastante decepcionante. La ciudad estaba superpoblada, lo que dificultó disfrutar de sitios famosos como el Coliseo y la Fuente de Trevi. A pesar de su importancia histórica, el encanto de la ciudad quedó ensombrecido por la abrumadora cantidad de turistas. Además, encontré que los restaurantes locales eran caros y la calidad de la comida decepcionante. Navegar por la ciudad también fue un problema debido al confuso transporte público y las calles congestionadas. Esperaba una experiencia más auténtica, pero desafortunadamente, se sintió demasiado comercializada y turística para mi gusto."},
                {"role":"assistant","content":"My recent trip to Rome was quite disappointing. The city was overcrowded, which made it difficult to enjoy the famous sites like the Colosseum and Trevi Fountain. Despite its historical significance, the city's charm was overshadowed by the overwhelming number of tourists. Additionally, I found the local restaurants overpriced and the food quality underwhelming. Navigating the city was also a hassle due to confusing public transport and congested streets. I was expecting a more authentic experience, but unfortunately, it felt too commercialized and touristy for my taste."},
                {"role":"user","content":f"Tanslate from Welsh to English: Fy mhrofiad diweddar gyda'r smartwatch newydd o gwmni XYZ oedd yn aruthrol. Roedd y dyluniad yn fodern ac yn chwaethus, a'r swyddogaethau monitro iechyd yn fanwl a chywir. Roedd gallu olrhain fy ymarfer corff a monitro cwsg yn hynod o ddefnyddiol. Roedd y bywyd batri yn wych hefyd, gan bara dyddiau heb angen ailwefru. Fodd bynnag, roedd y rhyngwyneb defnyddiwr braidd yn gymhleth i'w defnyddio ar y dechrau. Serch hynny, ar ôl ychydig o ddefnydd, daeth yn haws. Yn gyffredinol, roedd y smartwatch yn cyflawni fy anghenion yn berffaith."},
                {"role":"assistant","content":"My recent experience with the new smartwatch from XYZ company was outstanding. The design was modern and stylish, and the health monitoring functions were detailed and accurate. Being able to track my exercise and monitor my sleep was incredibly useful. The battery life was also great, lasting days without needing a recharge. However, the user interface was somewhat complex to use at first. Nevertheless, after a bit of usage, it became easier. Overall, the smartwatch perfectly met my needs."},
                {"role":"user","content": f"Tanslate from {leanguege} to English: {transcription}"}
                ]
    return completion(messages)

def get_resume(translation):
    system = {"role":"system", "content":"Generate a short resume of the text given."}
    messages = [system,
                {"role":"user","content":"I recently purchased the new 4K Ultra HD screen from XYZ brand, and I'm blown away by the quality it offers. The colors are incredibly vibrant, and the level of detail is stunning, especially when watching movies and shows. I've also used it for my gaming setup, and the experience is unparalleled. The response time is swift, and compatibility with various streaming platforms is a big plus. The design is sleek and looks great in my living room. However, I noticed that the built-in sound isn't as powerful as I expected, so I've had to use an external sound system for a more immersive experience. Overall, I'm very pleased with this purchase."},
                {"role":"assistant","content":"The user is impressed with the vibrant colors and image quality of their new 4K Ultra HD screen, finding it ideal for movies and gaming. The main drawback is the weak built-in sound, necessitating an external sound system. Overall, the user is very satisfied with the purchase."},
                {"role":"user","content":"My recent trip to Rome was quite disappointing. The city was overcrowded, which made it difficult to enjoy the famous sites like the Colosseum and Trevi Fountain. Despite its historical significance, the city's charm was overshadowed by the overwhelming number of tourists. Additionally, I found the local restaurants overpriced and the food quality underwhelming. Navigating the city was also a hassle due to confusing public transport and congested streets. I was expecting a more authentic experience, but unfortunately, it felt too commercialized and touristy for my taste."},
                {"role":"assistant","content":"The trip to Rome was disappointing due to overcrowding at tourist sites, overpriced and underwhelming local restaurants, and challenges with public transport. The experience felt overly commercialized and lacked authenticity."},
                {"role":"user","content": translation}
                ]
    return completion(messages)

def get_sentiment(transcription):
    system = {"role":"system", "content":"Guess wich sentiment. Choose between negative, neutral or positive."}
    messages = [system,
                {"role":"user","content":"I recently purchased the new 4K Ultra HD screen from XYZ brand, and I'm blown away by the quality it offers. The colors are incredibly vibrant, and the level of detail is stunning, especially when watching movies and shows. I've also used it for my gaming setup, and the experience is unparalleled. The response time is swift, and compatibility with various streaming platforms is a big plus. The design is sleek and looks great in my living room. However, I noticed that the built-in sound isn't as powerful as I expected, so I've had to use an external sound system for a more immersive experience. Overall, I'm very pleased with this purchase."},
                {"role":"assistant","content":"Positive"},
                {"role":"user","content":"My recent trip to Rome was quite disappointing. The city was overcrowded, which made it difficult to enjoy the famous sites like the Colosseum and Trevi Fountain. Despite its historical significance, the city's charm was overshadowed by the overwhelming number of tourists. Additionally, I found the local restaurants overpriced and the food quality underwhelming. Navigating the city was also a hassle due to confusing public transport and congested streets. I was expecting a more authentic experience, but unfortunately, it felt too commercialized and touristy for my taste."},
                {"role":"assistant","content":"Negative"},
                {"role":"user","content": transcription}
                ]
    return completion(messages)

def audio_response():
    # If the input is an audio then make the corresponding process.
    pass

def text_response():
    # If the input is text then process the response differently.
    pass