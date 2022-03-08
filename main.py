import os
import telebot
from telebot import types

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["inicio", "ayuda","start"])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="Proceso de Ingreso")
    button3 = types.KeyboardButton(text="Servicios Escolares")
    button4 = types.KeyboardButton(text="Finanzas")
    button5 = types.KeyboardButton(text="Becas")
    button6 = types.KeyboardButton(text="Vinculación")
    button7 = types.KeyboardButton(text="Recursos Materiales")

    keyboard.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, 'Hola! Bienvenido al Centro de Ayuda de la UPSLP. \nAcontinuacion se muestra los temas de ayuda. \n a) Oferta Educativa \n b) Proceso de Ingreso \nc) Servicios Escolares \nd) Finanzas \ne) Becas \nf) Vinculación\ng) Recursos Materiales', reply_markup=keyboard)

# Menu Oferta Educativa
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Oferta Educativa")
def func1(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Ingeniería en Telemática- Redes y Telecomunicaciones (ITEM-IRTEL)")
    button5 = types.KeyboardButton(text="2) Ingeniería en Tecnologías de la Información (ITI)")
    button6 = types.KeyboardButton(text="3) Ingeniería en Tecnologías de Manufactura (ITMA)")
    button7 = types.KeyboardButton(text="4) Ingeniería en Sistemas y Tecnologías Industriales (ISTI)")
    button8 = types.KeyboardButton(text="5) Licenciatura en Administración y Gestión (LAG)")
    button9 = types.KeyboardButton(text="6) Licenciatura en Mercadotecnia Internacional (LMI)")
    button10 = types.KeyboardButton(text="/inicio")
    keyboard.add(button4,button5,button6,button7,button8,button9,button10)

    bot.send_message(message.chat.id, "1) Ingeniería en Telemática- Redes y Telecomunicaciones (ITEM-IRTEL) \n2) Ingeniería en Tecnologías de la Información (ITI) \n3) Ingeniería en Tecnologías de Manufactura (ITMA) \n4) Ingeniería en Sistemas y Tecnologías Industriales (ISTI) \n5) Licenciatura en Administración y Gestión (LAG) \n6) Licenciatura en Mercadotecnia Internacional (LMI) \n\nLos Programas Educativos están conformados por 9 semestres", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Ingeniería en Telemática- Redes y Telecomunicaciones (ITEM-IRTEL)")
def func3(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación: \n   -Diseño y administración de redes \n   -Cableado estructurado \n   -Comunicaciones satelitales \n   -Antenas, comunicaciones inalámbricas y móviles", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Ingeniería en Tecnologías de la Información (ITI)")
def func4(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación: \n   Ingeniería de Software \n   Sistemas operativos \n   Diseño de bases de datos \n   Lenguajes de programación (PHP, Java, C, PERL) \n   Inteligencia Artificial", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3) Ingeniería en Tecnologías de Manufactura (ITMA)")
def func5(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación: \n   Automatización industrial \n   Mecatrónica \n   Diseño para manufactura \n   Lean manufacturing \n   Proceso de producción \n   Diseño de procesos de manufactura", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "4) Ingeniería en Sistemas y Tecnologías Industriales (ISTI)")
def func6(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación: \n   Sistemas de calidad. \n   Sistemas de producción de clase mundial \n   Logística y cadena de suministros \n   Productividad \n   Seguridad industrial \n   Lean manufacturing", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "5) Licenciatura en Administración y Gestión (LAG)")
def func7(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación: \n   Recursos humanos \n   Consultoría de negocios \n   Comunicación organizacional \n   Finanzas \n  Desarrollo emprendedor", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "6) Licenciatura en Mercadotecnia Internacional (LMI)")
def func8(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Oferta Educativa")
    button2 = types.KeyboardButton(text="/inicio")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Áreas de aplicación \n   Investigación de mercados \n   Logística y distribución \n   Servicio al cliente \n   Ventas profesionales \n   Comunicación integral de mercados \n   Consultoría de negocios", reply_markup=keyboard)

#Menu Proceso de Ingreso
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Proceso de Ingreso")
def func9(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Pasos para realizar el proceso de ingreso")
    button5 = types.KeyboardButton(text="2) Entrega de documentos")
    button6 = types.KeyboardButton(text="3) Costo de la ficha")
    button7 = types.KeyboardButton(text="4) Examen de ingreso- CENEVAL")
    button8 = types.KeyboardButton(text="5) Evaluaciones Institucionales")
    button9 = types.KeyboardButton(text="6) Publicación de resultados")
    button9 = types.KeyboardButton(text="/inicio")
    keyboard.add(button4,button5,button6,button7,button8,button9)

    bot.send_message(message.chat.id, "1) Pasos para realizar el proceso de ingreso \n2) Entrega de documentos \n3) Costo de la ficha \n4) Examen de ingreso- CENEVAL \n5) Evaluaciones Institucionales \n6) Publicación de resultados \nLos Programas ", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Pasos para realizar el proceso de ingreso")
def func10(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="https://ssu.upslp.edu.mx/ss/Admissions/ApplicationSelectEnabledForm.aspx", text="-	Ingresa a link y sigue los pasos de arriba")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "-	Llena la Solicitud de Nuevo Ingreso \n   -	Sube los documentos. \n   -	Descarga la ficha de pago referenciado. \n   -	Realiza el pago en el banco correspondiente, en ventanilla o cajero automático. \n   -	Tres días hábiles después de haber realizado el pago, el Departamento de Servicios Escolares te enviará un correo electrónico, a la cuenta que registraste en la Solicitud de Nuevo Ingreso, con las instrucciones para que realices tu registro en la plataforma de CENEVAL", reply_markup=keyboard)
  

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Entrega de documentos")
def func11(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Los documentos deberás adjuntarlos en la plataforma de la Universidad, después de finalizar el llenado de la Solicitud de Nuevo Ingreso.", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3) Costo de la ficha")
def func12(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "El costo de la ficha para presentar el examen de ingreso es de $1,170.00 (Mil ciento setenta pesos 00/100 M.N.)", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "4) Examen de ingreso- CENEVAL")
def func13(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "El examen de ingreso se aplicará el 22 de mayo", reply_markup=keyboard)
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "5) Evaluaciones Institucionales")
def func14(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Aplicación \n Las evaluaciones institucionales se llevarán a cabo en la plataforma Blackboard.\n Los aspirantes presentarán: \n   1.	Examen psicométrico, dividido en tres secciones: Razonamiento abstracto (tiempo asignado 20 minutos), razonamiento verbal (tiempo asignado 20 minutos) y razonamiento numérico (tiempo asignado 40 minutos) \n   2.	Examen de matemáticas con un tiempo asignado de 35 minutos. \n   3.	Para las carreras de ingeniería, realizarán un examen de Física, con un tiempo asignado de 35 minutos. \nLa duración total de las Evaluaciones Institucionales es de tres horas y está programado de manera que al término de esas tres horas el examen termine y ya no habrá forma de acceder nuevamente.  Si un aspirante ingresa después de su hora de inicio, sólo podrá presentar por el tiempo que le queda con respecto a la hora de cierre programada.", reply_markup=keyboard)



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "6) Publicación de resultados")
def func15(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Los resultados se publicarán únicamente en la página Web: www.upslp.edu.mx.", reply_markup=keyboard)


#Menu Servicios Escolares

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Servicios Escolares")
def func16(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Trámites")
    button5 = types.KeyboardButton(text="2) Dudas sobre los trámites")
    button6 = types.KeyboardButton(text="3) Costos de los trámites")
    button7 = types.KeyboardButton(text="4) Titulación")
    button9 = types.KeyboardButton(text="/inicio")

    keyboard.add(button4,button5,button6,button7,button9)

    bot.send_message(message.chat.id, "1) Trámites \n2) Dudas sobre los trámites \n3) Costos de los trámites \n4) Titulación ", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Trámites")
def func17(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="https://www.facebook.com/vinculacion.upslp", text="-	Ingresa a link \n")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Para realizar un trámite en Servicios Escolares debes agendar una cita en el siguiente enlace: \n ", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Dudas sobre los trámites")
def func18(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "El correo para consultar dudas es serviciosescolares@upslp.edu.mx", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3) Costos de los trámites")
def func19(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="http://www.upslp.edu.mx/upslp/?page_id=2423", text="-	Ingresa a link")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Consulta los costos de los trámites en Servicios Escolares en la página Web: ", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "4) Titulación")
def func20(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="http://www.upslp.edu.mx/upslp/?page_id=2449", text="-	Ingresa a link")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Consulta los trámites para el proceso de titulación en:", reply_markup=keyboard)


#Menu Finanzas
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Finanzas")
def func21(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button9 = types.KeyboardButton(text="/inicio")
    keyboard.add(button9)
    bot.send_message(message.chat.id, "Cualquier duda referente a pagos, envía un correo a  serviciosescolares@upslp.edu.mx", reply_markup=keyboard)

#Menu Becas
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Becas")
def func22(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Publicación de convocatorias")
    button5 = types.KeyboardButton(text="2) Consultas sobre las becas")
    button6 = types.KeyboardButton(text="3) Requisitos")
    button9 = types.KeyboardButton(text="/inicio")
    keyboard.add(button4,button5,button6,button9)

    bot.send_message(message.chat.id, "1) Publicación de convocatorias \n2) Consultas sobre las becas \n3) Requisitos", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Publicación de convocatorias")
def func23(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="www.upslp.edu.mx", text="-	Ingresa al link")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Las convocatorias de las becas se publican en la página Web de la UPSLP y en redes oficiales de la UPSLP. ", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Consultas sobre las becas")
def func24(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Para mayor información sobre las becas, envía un correo a becas_upslp@upslp.edu.mx", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3) Requisitos")
def func25(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Los requisitos varían dependiendo de cada convocatoria, por eso, es importante esperar a que se publique.", reply_markup=keyboard)

#menu Vinculación
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Vinculación")
def func26(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Eres estudiante de la UPSLP y deseas realizar prácticas profesionales")
    button5 = types.KeyboardButton(text="2) Eres egresado de la UPSLP y buscas empleo")
    button9 = types.KeyboardButton(text="/inicio")
    keyboard.add(button4,button5,button9)

    bot.send_message(message.chat.id, "1) Eres estudiante de la UPSLP y deseas realizar prácticas profesionales \n2) Eres egresado de la UPSLP y buscas empleo", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Eres estudiante de la UPSLP y deseas realizar prácticas profesionales")
def func27(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="https://www.facebook.com/vinculacion.upslp", text="-	Ingresa al link")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Consulta las vacantes en el link de abajo o envía un correo a vinculacion@upslp.edu.mx ", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Eres egresado de la UPSLP y buscas empleo")
def func28(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="https://www.facebook.com/vinculacion.upslp", text="-	Ingresa al link")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "Consulta las vacantes en el link de abajo o envía un correo con tu CV  a vinculacion@upslp.edu.mx ", reply_markup=keyboard)

#menu Recursos materiales
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Recursos Materiales")
def func29(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button4 = types.KeyboardButton(text="1) Tarjetón vehicular")
    button5 = types.KeyboardButton(text="2) Trámite del tarjetón")
    button6 = types.KeyboardButton(text="3) Entrega de tarjetón en proceso de titulación")
    button9 = types.KeyboardButton(text="/inicio")
    keyboard.add(button4,button5,button6,button9)

    bot.send_message(message.chat.id, "1) Tarjetón vehicular \n2) Trámite del tarjetón \n3) Entrega de tarjetón en proceso de titulación", 
    reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1) Tarjetón vehicular")
def func30(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "La UPSLP cuenta con estacionamiento para estudiantes, docentes y administrativos que cuenten con vehículo; para hacer uso del mismo, es necesario realizar el trámite de tarjetón vehicular en el área de Recursos Materiales, el cual permite identificarlos como parte de la comunidad universitaria y como seguridad para quienes la integran.", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2) Trámite del tarjetón")
def func31(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Para tener acceso al estacionamiento se deberá tramitar el tarjetón vehicular en el área de Recursos Materiales indicando marca, modelo, color y mostrando la tarjeta de circulación; así como presentando la credencial oficial UPSLP.", reply_markup=keyboard)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3) Entrega de tarjetón en proceso de titulación")
def func32(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Para el proceso de titulación, se deberá entregar el tarjetón al área de Recursos Materiales.", reply_markup=keyboard)

bot.infinity_polling()
