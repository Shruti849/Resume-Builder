from telegram.ext import ConversationHandler, Filters, Updater, CommandHandler, MessageHandler, CallbackContext,CallbackQueryHandler
from dbhelper import Session, engine
import logging
from models import User
from datetime import datetime
from telegram import constants, Update, InlineKeyboardButton, InlineKeyboardMarkup, replymarkup
import os
import requests
from multiprocessing import Process
import warnings
warnings.filterwarnings("ignore")

TOKEN = '5396584409:AAGEFkgFAu8B3Qut8VmWTtI5KGgYtfZET-g'  
FOLDERNAME_USERWORKS = 'static/userworks/'
if not os.path.isdir(FOLDERNAME_USERWORKS):
    os.mkdir(FOLDERNAME_USERWORKS)

register_timeout_time = 480
editprofile_timeout_time = 480

END = ConversationHandler.END
SELECTING_ACTION, SELECTED_NAME, SELECTED_EMAIL, SELECTED_PHONE_NO ,SELECTED_ABOUT,SELECTED_SKILLS,SELECTED_PROJECT,SELECTED_LANGUAGE= range(8)
NAME, GENDER, EMAIL_ID, PHONE_NO, ADDRESS,SCHOOL_10th,YEAR_10th, PERCENT_10th, SELECTIONCLASS, BOTH_COMPLETE,COLLEGE_12th,YEAR_12th, PERCENT_12th,DIPLOMA_UNIVERSITY_NAME,DIPLOMA_COURCE_NAME,DIPLOMA_YEAR,DIPLOMA_PERCENT,GRADUATION_UNIVERSITY_NAME,GRADUATION_COURCE_NAME,GRADUATION_YAER,GRADUATION_PERCENT,POST_GRADUATION_UNIVERSITY_NAME,POST_GRADUATION_COURCE_NAME,POST_GRADUATION_YEAR, POST_GRADUATION_PERCENT, LANGUAGELINK, TECHNICALSKILLS, PROJECT, ABOUT = range(
    29)
RECORD_WORKPHOTO = range(1)
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)
logger = logging.getLogger(__name__)


def save_file_locally(filepath_to_download, filename_to_store):
    response = requests.get(filepath_to_download)
    final_file_path = f"{FOLDERNAME_USERWORKS}{filename_to_store}"
    try:
        logger.info(f"Inside /addlog. Saving image locally")
        with open(final_file_path, 'wb') as f:
            f.write(response.content)
        logger.info("Image Saved locally..")
        return True
    except:
        logger.info("Image could not be saved locally..")
        return False


def start(update, context):
    chat_id = update.message.chat_id
    with Session() as session:
        user = User.get_user_by_chatid(session=session, chat_id=chat_id)
        if not user:
            update.message.reply_text("Welcome to CTO Profile :) !\n"
                                      "You can use this Bot to create your Resume .\n"
                                      "For this you have to register by adding all the details.For registeration use\n"
                                      " /register ")
        else:
            update.message.reply_text("You have already registered with following details\n"
                                      f"Name - {user.name}\n"
                                      f"Gender -{user.gender}\n"
                                      f"Emaild - {user.email_id}\n"
                                      f"Phone_no - {user.phone_no}\n"
                                      f"Address - {user.address}\n"
                                      f"10th School - {user.school_10th}\n"
                                      f"Passing Year Of 10th - {user.year_10th}\n"
                                      f"10th Percentage - {user.percent_10th}\n"
                                      f"12th College - {user.college_12th}\n"
                                      f"Passing Year 12th - {user.year_12th}\n"
                                      f"12th Percentage - {user.percent_12th}\n"
                                      f"Diploma College - {user.diploma_university_name}\n"
                                      f"Diploma Cource Name - {user.diploma_cource_name}\n"
                                      f"Passing Year Of Diploma - {user.diploma_year}\n"
                                      f"Diploma Percentage - {user.diploma_percent}\n"
                                      f"Graduation University Name - {user.graduation_university_name}\n"
                                      f"Graduation Cource Name - {user.graduation_cource_name}\n"
                                      f"Graduation Passing Year - {user.graduation_year}\n"
                                      f"Graduation Percentage - {user.graduation_percent}\n"
                                      f"Post Graduation University Name - {user.graduation_university_name}\n"
                                      f"Post Graduation Cource Name - {user.post_graduation_cource_name}\n"
                                      f"Post Graduation Passing Year - {user.post_graduation_year}\n"
                                      f"Post Graduation Percentage- {user.post_graduation_percent}\n"
                                      f"Languages Known - {user.lang_link}\n"
                                      f"Technical Skills - {user.technical_skills}\n"
                                      f"Project -{user.project}\n"
                                      f"About-{user.about}\n"
                                      )


def check_if_user_exists(chat_id):
    """ Return user from database (returns None implicitly if not found) """
    # We will directly check from database each time for this command in particular. So we won't use get current user for this.
    with Session() as session:
        user = User.get_user_by_chatid(session=session, chat_id=chat_id)
        return user


def register(update, context):
    """ Registration """
    chat_id = update.message.chat_id
    user = check_if_user_exists(chat_id)
    if not user:
        logger.info(f"Inside /register. User not found. Going into registration flow. ")
    
        update.message.reply_text("Let's get you registered.\nEnter your full name")
        return NAME
    else:
        logger.info(f"Inside /register. User found. Details shown")
        # These three properties shall come from daatabase. We'll fix it, but first let's complete the conversation flow.
        update.message.reply_text(f"You are already registered with the following details\n"

                                  f"Name - {user.name}\n"
                                  f"Gender -{user.gender}\n"
                                  f"Emaild - {user.email_id}\n"
                                  f"Phone_no - {user.phone_no}\n"
                                  f"Address - {user.address}\n"
                                  f"10th School - {user.school_10th}\n"
                                  f"Passing Year Of 10th - {user.year_10th}\n"
                                  f"Percent of 10th - {user.percent_10th}\n"
                                  f"12th College - {user.college_12th}\n"
                                  f"Passing Year 10th - {user.year_12th}\n"
                                  f"12th Percentage - {user.percent_12th}\n"
                                  f"Diploma College - {user.diploma_university_name}\n"
                                  f"Diploma Cource Name - {user.diploma_cource_name}\n"
                                  f"Passing Year Of Diploma - {user.diploma_year}\n"
                                  f"Diploma Percentage - {user.diploma_percent}\n"  
                                  f"Graduation University Name - {user.graduation_university_name}\n"
                                  f"Graduation Cource Name - {user.graduation_cource_name}\n"
                                  f"Graduation Passing Year - {user.graduation_year}\n"
                                  f"Graduation Percentage - {user.graduation_percent}\n"
                                  f"Post Graduation University Name - {user.graduation_university_name}\n"
                                  f"Post Graduation Cource Name - {user.post_graduation_cource_name}\n"
                                  f"Post Graduation Passing Year - {user.post_graduation_year}\n"
                                  f"Post Graduation Percentage- {user.post_graduation_percent}\n"
                                  f"languagelink - {user.lang_link}\n"
                                  f"technicalskills - {user.technical_skills}\n"
                                  f"project - {user.project}\n"
                                  f"about - {user.about}\n"
                                  )
        update.message.reply_text("Use /editprofile command to edit your profile")

        return ConversationHandler.END


def name(update, context):
    msg = update.message.text
    if len(msg) > 30:
        update.message.reply_text('Too long a name. Try shorter one.')
        logger.info(f"Inside /register. Got very very long name > 30 - {msg}")
        return NAME
    elif len(msg) < 5:
        update.message.reply_text('Too short name!.\nPlease provide full name.')
        return NAME
    keyboard = [
        [
            InlineKeyboardButton("Male", callback_data='selectmale'),
            InlineKeyboardButton("Female", callback_data='selectfemale'),
            InlineKeyboardButton("Trangender", callback_data='selecttrans'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(f"Nice to know you, {msg}\n Please select the Gender ", reply_markup=reply_markup)
    user_data = context.user_data
    user_data['name'] = msg
    user_data['chat_id'] = update.effective_message.chat_id
    logger.info(f"Inside /register. Got name - {user_data['name']}")
    # We are storing this user data in the storage provided by TG, and at once we'll store it in db'
    return GENDER


def gender(update, context):
    user_data = context.user_data
    query = update.callback_query
    query.answer()
    # print("-------------------------------------------")
    # print(query.answer)
    # print(query.answer())
    if query.data == 'selectmale':
        user_data['gender'] = 'male'
        query.edit_message_text(text=f"Now please enter your Email Id ")
        return EMAIL_ID
    elif query.data == 'selectfemale':
        user_data['gender'] = 'Female'
        query.edit_message_text(text=f"Now please enter your Email Id")
        return EMAIL_ID
    elif query.data == 'selecttrans':
        user_data['gender'] = 'trans'

        query.edit_message_text(text=f"Now please enter your Email Id")
        return EMAIL_ID
    else:
        query.edit_message_text(text=f"Something is wrong. Try again later.")
        return ConversationHandler.END


def check_if_email_already_exists(email_id):
    with Session() as session:
        res = session.query(User).filter(User.email_id == email_id).first()
        return res


def email(update, context):
    email_id = update.message.text
    email_id = email_id.strip()
    old_email_flag = check_if_email_already_exists(email_id)
    if old_email_flag:
        update.message.reply_text(f"Email already in use.\nUse another one.")
        logger.info(f"/register - email --> ALREADY EXIST: {email_id}")
        return EMAIL_ID
    user_data = context.user_data
    user_data['email_id'] = email_id
    update.message.reply_text("Got email_id.\n Enter a valid mobile no.")
    logger.info(f"Inside /register. Got email - {user_data['email_id']}")
    return PHONE_NO


def wrong_email(update, context):
    logger.info(f"Inside /register. Got wrong email id. Asked to try again.")
    update.message.reply_text("Wrong email. Try again")
    return EMAIL_ID


def reg_cancel(update, context):
    logger.info(f"Inside /reg_cancel. Some error. ")
    update.message.reply_text('Byebye!')
    clear_reg_context_userdata(context=context)
    return ConversationHandler.END


def timeout_register(update, context):
    update.message.reply_text(f'Timeout. Kindly /register again. (Timeout limit - {register_timeout_time} sec)')
    logger.info(f"Timeout for /addlog")
    chat_data = context.chat_data
    chat_data.clear()
    logger.info(f"context.user_data cleared")


def phone_no(update, context):
    phone_no = update.message.text
    try:
        phone_no = int(phone_no)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return PHONE_NO
    if phone_no > 10 and phone_no < 10:
        update.message.reply_text("Phone no must be ten digit.")
        return PHONE_NO
    user_data = context.user_data
    user_data['phone_no'] = phone_no
    update.message.reply_text(f"Got your phone number .Now enter your address  ")
    logger.info(f"Inside /register. Got contact no - {user_data['phone_no']}")
    return ADDRESS


def address(update, context):
    address = update.message.text
    user_data = context.user_data
    user_data['address'] = address
    update.message.reply_text(f"Got your address.\n Next, Please Enter your class 10th details. ")
    update.message.reply_text(f" Please Enter your 10th School name. ")
    return SCHOOL_10th


def school_10th(update, context):
    school_10th = update.message.text
    user_data = context.user_data
    user_data['school_10th'] = school_10th
    update.message.reply_text(" Next Enter your Class 10th passing year.\nExample- 2001-2002")
    return YEAR_10th


def year_10th(update, context):
    year_10th = update.message.text
    try:
        year_10th = str(year_10th)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return year_10th

    user_data = context.user_data
    user_data['year_10th'] = year_10th
    update.message.reply_text(f"Got your passing year.\nPleased Enter your  10th percentage. ")
    logger.info(f"Inside /register. Got 10th passing year - {user_data['year_10th']}")
    return PERCENT_10th

def percent_10th(update, context):
    percent_10th = update.message.text
    user_data = context.user_data
    user_data['percent_10th'] = percent_10th
    try:
        percent_10th = int(percent_10th)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return PERCENT_10th
    if percent_10th > 100.00:
        update.message.reply_text("Invalid .Please enter it in proper way.")
        return PERCENT_10th

    keyboard = [
        [
            InlineKeyboardButton("Class 12th", callback_data='select12th'),
            InlineKeyboardButton("Diploma", callback_data='selectdiploma'),
            InlineKeyboardButton("Both", callback_data='selectboth'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Got your  Class 10th Datails .\n Have you done class 12th or diploma or both.",
                              reply_markup=reply_markup)
    return SELECTIONCLASS


def selectionclass(update, context):
    query = update.callback_query
    query.answer()
    print("-------------------------------------------")
    print(query.answer)
    print(query.answer())
    if query.data == 'select12th':
        query.edit_message_text(text=f"Enter your Class 12th College name.  ")
        return COLLEGE_12th
    elif query.data == 'selectdiploma':
        query.edit_message_text(text=f"Enter your diploma college name ")
        return DIPLOMA_UNIVERSITY_NAME
    elif query.data == 'selectboth':
        query.edit_message_text(text=f"Enter class 12th and diploma details respectively leaving one space:")
        return BOTH_COMPLETE
    else:
        query.edit_message_text(text=f"Something is wrong. Try again later.")
        return ConversationHandler.END


def both_complete(update, context):
    p1 = Process(target=college_12th(update, context))
    p1.start()
    p2 = Process(target=diploma_university_name(update, context))
    p2.start()
    return GRADUATION_UNIVERSITY_NAME



def college_12th(update, context):
    college_12th = update.message.text
    user_data = context.user_data
    user_data['college_12th'] = college_12th
    update.message.reply_text(" Got your College name .\n Now Enter your Class 12th passing year.\nExample- 2001-2002")
    return YEAR_12th


def year_12th(update, context):
    year_12th = update.message.text
    try:
        year_12th = str(year_12th)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return year_12th

    user_data = context.user_data
    user_data['year_12th'] = year_12th
    update.message.reply_text(f"Got your passing year.\n Now enter your class 12th percentage . ")
    logger.info(f"Inside /register. Got 12th passing year- {user_data['year_12th']}")
    return PERCENT_12th

def percent_12th(update, context):
    percent_12th = update.message.text
    user_data = context.user_data
    user_data['percent_12th'] = percent_12th
    try:
        percent_12th = int(percent_12th)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return PERCENT_12th
    if percent_12th > 100.00:
        update.message.reply_text("Invalid .Please enter it in proper way.")
        return PERCENT_12th
    update.message.reply_text("Got your class 12th details.\n Next Enter your university name from  where you completed your graduation ")

    return GRADUATION_UNIVERSITY_NAME



def diploma_university_name(update, context):
    diploma_university_name = update.message.text
    user_data = context.user_data
    user_data['diploma_university_name'] = diploma_university_name
    update.message.reply_text(" Got your Cource name .\n Now Enter your  name of the cource in diploma ")
    return DIPLOMA_COURCE_NAME

def diploma_cource_name(update, context):
    diploma_cource_name = update.message.text
    user_data = context.user_data
    user_data['diploma_cource_name'] = diploma_cource_name
    update.message.reply_text(" Got your Cource name .\n Now Enter your diploma passing year.\nExample- 2001-2002")
    return DIPLOMA_YEAR


def diploma_year(update, context):
    diploma_year = update.message.text
    try:
        diploma_year = str(diploma_year)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return diploma_year

    user_data = context.user_data
    user_data['diploma_year'] = diploma_year
    update.message.reply_text(f"Got your passing year.\n Now enter your diploma  percentage . ")
    logger.info(f"Inside /register. Got diploma passing year - {user_data['diploma_year']}")
    return DIPLOMA_PERCENT

def diploma_percent(update, context):
    diploma_percent = update.message.text
    user_data = context.user_data
    user_data['diploma_percent'] = diploma_percent
    try:
        diploma_percent = int(diploma_percent)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return DIPLOMA_PERCENT
    if diploma_percent > 100.00:
        update.message.reply_text("Invalid .Please enter it in proper way.")
        return DIPLOMA_PERCENT
    update.message.reply_text("Got your diploma details.\n Next Enter your Graduation university/College name from where you completed your graduation")
    return GRADUATION_UNIVERSITY_NAME



def graduation_university_name(update, context):
    graduation_university_name = update.message.text
    user_data = context.user_data
    user_data['graduation_university_name'] = graduation_university_name
    update.message.reply_text(" Got your cource name .\n Next, Enter your graduation cource name.\n Ex.  BSC/BA/BCOM....")
    return GRADUATION_COURCE_NAME

def graduation_cource_name(update, context):
    graduation_cource_name = update.message.text
    user_data = context.user_data
    user_data['graduation_cource_name'] = graduation_cource_name
    update.message.reply_text(" Got your cource name .\n Now Enter your graduation passing year.\nExample- 2001-2002")
    return GRADUATION_YAER


def graduation_year(update, context):
    graduation_year = update.message.text
    try:
        graduation_year = str(graduation_year)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return graduation_year

    user_data = context.user_data
    user_data['graduation_year'] = graduation_year
    update.message.reply_text(f"Got your passing year.\n Now enter your  graduation percentage . ")
    logger.info(f"Inside /register. Got your graduation passing year - {user_data['graduation_year']}")
    return GRADUATION_PERCENT

def graduation_percent(update, context):
    graduation_percent = update.message.text
    user_data = context.user_data
    user_data['graduation_percent'] = graduation_percent
    try:
        graduation_percent = int(graduation_percent)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return GRADUATION_PERCENT
    if graduation_percent > 100.00:
        update.message.reply_text("Invalid .Please enter it in proper way.")
        return GRADUATION_PERCENT
    update.message.reply_text("Got your graduation details.\n Next Enter your Post Graduation university/College name from where you completed your graduation")
    # update.message.reply_text("If you have not done post graduation then type NONE ")
    return POST_GRADUATION_UNIVERSITY_NAME


def post_graduation_university_name(update, context):
    post_graduation_university_name = update.message.text
    user_data = context.user_data
    user_data['post_graduation_university_name'] = post_graduation_university_name
    update.message.reply_text(" Got your cource name .\n Next Enter your Post graduation cource name.\n EX. MSC/ MA/MCOM...")
    return POST_GRADUATION_COURCE_NAME

def post_graduation_cource_name(update, context):
    post_graduation_cource_name = update.message.text
    user_data = context.user_data
    user_data['post_graduation_cource_name'] = post_graduation_cource_name
    update.message.reply_text(" Got your College name .\n Now Enter your post graduation passing year.\nExample- 2001-2002")
    return POST_GRADUATION_YEAR


def post_graduation_year(update, context):
    post_graduation_year = update.message.text
    try:
        post_graduation_year = str(post_graduation_year)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return post_graduation_year

    user_data = context.user_data
    user_data['post_graduation_year'] = post_graduation_year
    update.message.reply_text(f"Got your passing year.\n Now enter your post graduation percentage . ")
    logger.info(f"Inside /register. Got post graduation passing year - {user_data['post_graduation_year']}")
    return POST_GRADUATION_PERCENT

def post_graduation_percent(update, context):
    post_graduation_percent = update.message.text
    user_data = context.user_data
    user_data['post_graduation_percent'] = post_graduation_percent
    try:
        post_graduation_percent = int(post_graduation_percent)
    except:
        update.message.reply_text("Only numbers are allowed.")
        return POST_GRADUATION_PERCENT
    if post_graduation_percent > 100.00:
        update.message.reply_text("Invalid .Please enter it in proper way.")
        return POST_GRADUATION_PERCENT
    update.message.reply_text("Got your post graduation details.")
    update.message.reply_text("Next Enter Which Langauage You Know.\n (Click On /langdone  once done)")
    return LANGUAGELINK


def lang_link(update, context):
    lang = update.message.text
    user_data = context.user_data
    if not user_data.get('lang'):
        user_data['lang'] = list()
        user_data['lang'].append(lang)
    else:
        user_data['lang'].append(lang)
    return LANGUAGELINK


def langdone(update, context):
    user_data = context.user_data
    update.message.reply_text("Noted the Languages.\n Enter the technical skills one by one (say /techdone once done)")
    if not user_data.get('lang'):
        user_data['lang'] = None
    user_data['lang'] = ','.join(user_data['lang'])
    return TECHNICALSKILLS


def technical_skills(update, context):
    skill = update.message.text
    print(skill)
    user_data = context.user_data
    if not user_data.get('skill'):
        user_data['skill'] = list()
        user_data['skill'].append(skill)
    else:
        user_data['skill'].append(skill)
    return TECHNICALSKILLS


def techdone(update, context):
    user_data = context.user_data
    if not user_data.get('skill'):
        user_data['skill'] = None
    user_data['skill'] = ','.join(user_data['skill'])
    update.message.reply_text("Noted the Technical skills.")
    update.message.reply_text(f"Enter your Projects. Click on command /projectdone once done. ")
    return PROJECT


def projects(update, context):
    prjt = update.message.text
    print(prjt)
    user_data = context.user_data
    if not user_data.get('prjt'):
        user_data['prjt'] = list()
        user_data['prjt'].append(prjt)
    else:
        user_data['prjt'].append(prjt)
    return PROJECT


def projectdone(update, context):
    user_data = context.user_data
    if not user_data.get('prjt'):
        user_data['prjt'] = None
    user_data['prjt'] = ','.join(user_data['prjt'])
    update.message.reply_text(
        f"Got your Project Details \n Tell us something about yourself(ex : WorkExperience),Hobby,Strength")
    return ABOUT


def about(update, context):
    abt = update.message.text
    user_data = context.user_data
    user_data['abt'] = abt
    update.message.reply_text(" Upload your photo .")
    return RECORD_WORKPHOTO


def record_workphoto(update, context):
    with Session() as session:
        update.message.reply_text('Image Received. Processing..')
        our_file = update.effective_message.photo[-1]
        if our_file:
            try:
                file_id = our_file.file_id
                # file_unique_id = our_file.file_unique_id
                actual_file = our_file.get_file()
                filepath_to_download = actual_file['file_path']
                ext = filepath_to_download.split('.')[-1]
                filename_to_store = f"{file_id}.{ext}"
                logger.info(f"Inside /register. Got photo. Saving photo as- {filename_to_store}")
                update.message.reply_chat_action(action=constants.CHATACTION_UPLOAD_PHOTO)

                status = save_file_locally(filepath_to_download=filepath_to_download,
                                           filename_to_store=filename_to_store)
                if status:
                    update.message.reply_text('Image uploaded successfully..')
                else:
                    update.message.reply_text("Image not uploaded. Plz try again")

                user_data = context.user_data
                final_file_path = f"{FOLDERNAME_USERWORKS}{filename_to_store}"
                user_data['photo'] = final_file_path
                logger.info(f"Inside /register. Got photo. Final work links - {user_data['photo']}")
            except:
                logger.error(f"Update {update} caused error WHILE SAVING PHOTO- {context.error}")
                logger.error(f"Exception while saving photo", exc_info=True)

        save_user(update, context)
        return ConversationHandler.END  # we want to continue calling same function until /done is written explicitly.


def donelinks(update, context):
    chat_data = context.chat_data
    if not chat_data.get('work_link_temp'):
        chat_data['work_links'] = None
    else:
        chat_data['work_links'] = ','.join(chat_data['work_link_temp'])
    update.message.reply_text('Next, upload photos of code/output if any (Use /donephotos once done).')
    return RECORD_WORKPHOTO


def donephotos(update, context):
    chat_data = context.chat_data
    if not chat_data.get('work_photo_temp'):
        chat_data['work_photos'] = None
        logger.info(f"Inside /submitgigstep. /donephotos. No work photos so storing chat_data['work_photos'] to None")
    else:
        chat_data['work_photos'] = ',,,'.join(chat_data[
                                                  'work_photo_temp'])  # deliberately using this instead of comma, bcz if user somehow enters , in his work links, then it'll be split unnecessarily. so we want some unique identifier.
    return ConversationHandler.END


def no_text_allowed(update, context):
    update.message.reply_text("Only photos are accepted. Submit photo of your work for the respective step!")
    return RECORD_WORKPHOTO


def save_user(update, context: CallbackContext):
    user_data = context.user_data
    name = user_data['name'].title()
    gender = user_data['gender']
    email_id = user_data['email_id']
    phone_no = user_data['phone_no']
    address = user_data['address']
    school_10th = user_data['school_10th']
    year_10th = user_data['year_10th']
    percent_10th = user_data['percent_10th']
    college_12th = user_data['college_12th']
    year_12th = user_data['year_12th']
    percent_12th = user_data['percent_12th']
    if not user_data.get('diploma_university_name'):
        user_data['diploma_university_name'] = None
        diploma_university_name = user_data['diploma_university_name']
    else:
        diploma_cource_name = user_data['diploma_university_name']
    if not user_data.get('diploma_cource_name'):
        user_data['diploma_cource_name'] = None
        diploma_cource_name = user_data['diploma_cource_name']
    else:
        diploma_cource_name = user_data['diploma_cource_name']
    if not user_data.get('diploma_year'):
        user_data['diploma_year'] = None
        diploma_year = user_data['diploma_year']
    else:
        diploma_year = user_data['diploma_year']
    if not user_data.get('diploma_percent'):
        user_data['diploma_percent'] = None
        diploma_percent = user_data['diploma_percent']
    else:
        diploma_percent = user_data['diploma_percent']
    graduation_university_name = user_data['graduation_university_name']
    graduation_cource_name = user_data['graduation_cource_name']
    graduation_year = user_data['graduation_year']
    graduation_percent = user_data['graduation_percent']
    post_graduation_university_name = user_data['post_graduation_university_name']
    post_graduation_cource_name = user_data['post_graduation_cource_name']
    post_graduation_year = user_data['post_graduation_year']
    post_graduation_percent = user_data['post_graduation_percent']
    lang_link = user_data['lang']
    technical_skills = user_data['skill']
    project = user_data['prjt']
    about = user_data['abt']
    record_workphoto = user_data['photo']

    chat_id = user_data['chat_id']

    user = User(chat_id=chat_id, name=name, gender=gender, email_id=email_id, phone_no=phone_no,address=address, school_10th =school_10th,year_10th=year_10th,
                percent_10th=percent_10th,college_12th=college_12th,year_12th=year_12th,percent_12th=percent_12th,
                 diploma_university_name = diploma_university_name,diploma_cource_name=diploma_cource_name,diploma_year=diploma_year,diploma_percent=diploma_percent,graduation_university_name=graduation_university_name,graduation_cource_name=graduation_cource_name,graduation_year=graduation_year,graduation_percent=graduation_percent,post_graduation_university_name=post_graduation_university_name,
                post_graduation_cource_name=post_graduation_cource_name,post_graduation_year=post_graduation_year,post_graduation_percent=post_graduation_percent, lang_link=lang_link, technical_skills=technical_skills,
                project=project, about=about, record_workphoto=record_workphoto, created_at=datetime.utcnow(),
                updated_at=datetime.utcnow())
                
    print(user)
    with Session() as session:
        session.add(user)
        try:
            session.commit()
            name=name.lower()
            name=name.replace(' ','-')

            update.message.reply_text(f"That's it . You have successfully registered yourself.\nUse Following link to view your resume: http://127.0.0.1:5000/{name}")
            update.message.reply_text(f" Have a good day !")
 
            update.message.reply_text("Use /editprofile command to edit your profile")
            # update.message.reply_text(f"You can use following link to see your resume here: {https://127.0.0.1:5000/{name}}")

            user_data.clear()
            logger.info("user_data cleared.")
        except:
            session.rollback()
            clear_reg_context_userdata(context=context)
            logger.error(f"Some error saving user while registering!", exc_info=True)
            update.message.reply_text("Something wrong. Please try later or contact admin..")
        return END


def clear_reg_context_userdata(context):
    context.user_data.clear()
    logger.info(f"context.user_data cleared")


def editprofile(update, context):
    with Session() as session:
        chat_id = update.effective_message.chat_id
        user = check_if_user_exists(chat_id=chat_id)
        if user:
            keyboard = [
                [
                    InlineKeyboardButton("Name", callback_data='editname'),
                    InlineKeyboardButton("Email", callback_data='editemail'),
                    InlineKeyboardButton("Phone_no", callback_data='editphone'),
                    

                ],
                 [
                    InlineKeyboardButton("Language", callback_data='editlanguage'),                
                    InlineKeyboardButton("Technical_Skills", callback_data='edittechnical_skills'),
                    InlineKeyboardButton("Project", callback_data='editproject'),
                 ],
                 [
                    InlineKeyboardButton("About", callback_data='editabout')                 

                 ]
                 
            ]
            name=user.name.lower()
            name=name.replace(' ','-')

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(
                f"Your current profile details\nName - {user.name}\nEmail - {user.email_id}\nPhone Number-{user.phone_no}\nLanguage-{user.lang_link}\nTechnical Skills-{user.technical_skills}\nProjects-{user.project}\nAbout-{user.about}\n(Use /canceledit to cancel).\nUse Following link to view your updated resume: http://127.0.0.1:5000/{name}",
                reply_markup=reply_markup)
            
            
            # update.message.reply_text(f"That's it . You have successfully edit your profile.\nUse Following link to view your updated resume: http://127.0.0.1:5000/{name}")

 
            
            return SELECTING_ACTION


def editwhat(update: Update, context):
    chat_id = update.effective_message.chat_id
    with Session() as session:
        user = check_if_user_exists(chat_id=chat_id)
        if not user:
            return
        query = update.callback_query
        query.answer()
        if query.data == 'editname':
            query.edit_message_text(text=f"Enter your new name -:\n(/cancelthis to cancel)")
            return SELECTED_NAME
        elif query.data == 'editemail':
            query.edit_message_text(text=f"Enter your new email -:\n(/cancelthis to cancel)")
            return SELECTED_EMAIL
        elif query.data == 'editphone':
            query.edit_message_text(text=f"Enter your new phone_no -: \n(/cancelthis to cancel)")
            return SELECTED_PHONE_NO
        elif query.data == 'editlanguage':
            query.edit_message_text(text=f"Enter your new langauges that you know -: \n(/cancelthis to cancel)")
            return SELECTED_LANGUAGE
        elif query.data == 'edittechnical_skills':
            query.edit_message_text(text=f"Enter your new technical skills -:\n(/cancelthis to cancel) ")
            return SELECTED_SKILLS
        elif query.data == 'editproject':
            query.edit_message_text(text=f"Enter your new project names -:\n(/cancelthis to cancel) ")
            return SELECTED_PROJECT
        elif query.data == 'editabout':
            query.edit_message_text(text=f"Enter about yourself(ex : WorkExperience),Hobby,Strength \n (/cancelthis to cancel)")
            return SELECTED_ABOUT

        else:
            query.edit_message_text(text=f"Something is wrong. Try again later.")
            return ConversationHandler.END


def enter_new_name(update: Update, context: CallbackContext):
    with Session() as session:
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        msg = update.message.text
        if user:
            edited_user = user.update_name(session=session, name=msg)
            update.message.reply_text(f"Your new name is - {edited_user.name}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")

        return END


def enter_new_email(update: Update, context: CallbackContext):
    with Session() as session:
        msg = update.message.text
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        if user:
            if user.email_id == msg.strip():
                update.message.reply_text(
                    f"New and old email are same. No changes made. (/editprofile again for any other changes)")
                return END
            is_old_email = check_if_email_already_exists(email_id=msg)
            if is_old_email:
                update.message.reply_text(f"This email already in use, try another one.")
                return SELECTED_EMAIL

            edited_user = user.update_email(session=session, email=msg)
            update.message.reply_text(f"Your new Email is- {edited_user.email_id}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")

        return END


def enter_phone_no(update: Update, context: CallbackContext):
    with Session() as session:
        phone_no = update.message.text
        try:
            phone_no = int(phone_no)
        except:
            update.message.reply_text("Only numbers are allowed.")
            return SELECTED_PHONE_NO
        if phone_no > 10 and phone_no < 10:
            update.message.reply_text("Phone no must be ten digit.")
            return SELECTED_PHONE_NO

        chat_id = update.effective_message.chat_id
        user = check_if_user_exists(chat_id=chat_id)
        if user:
            if user.phone_no == phone_no:
                update.message.reply_text(
                    f"New and old phone_no are same. No changes made. (/editprofile again for any other changes)")
                return END
            edited_user = user.update_phone_no(session=session, phone_no=phone_no)
           
            update.message.reply_text(f"Your new phone number is - {edited_user.phone_no}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")
        return END


def enter_new_languages(update: Update, context: CallbackContext):
    with Session() as session:
        lang= update.message.text
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        user_data = context.user_data
        if user:
            user_data['lang'] = list()
            user_data['lang'].append(lang)
            edited_user_data = user.update_lang_link(session=session, lang_link=lang)
            update.message.reply_text(f"Your new langauges are - {edited_user_data.lang_link}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")
        
        else:
            user_data['lang'].append(lang) 
        return END


def enter_new_technical_skills(update: Update, context: CallbackContext):
    with Session() as session:
        skills= update.message.text
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        user_data = context.user_data
        if user:
            user_data['skills'] = list()
            user_data['skills'].append(skills)
            edited_user_data = user.update_technical_skills(session=session, technical_skills=skills)
            update.message.reply_text(f"Your new technical skills are - {edited_user_data.technical_skills}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")
        
        else:
            user_data['skills'].append(skills) 
        return END

def enter_new_project(update: Update, context: CallbackContext):
    with Session() as session:
        project = update.message.text
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        user_data = context.user_data
        if user:
            user_data['project'] = list()
            user_data['project'].append(project)
            edited_user_data = user.update_project(session=session, project=project)
            update.message.reply_text(f"Your new projects are - {edited_user_data.project}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")
        
        else:
            user_data['project'].append(project) 
        return END


def enter_new_about(update: Update, context: CallbackContext):
    with Session() as session:
        chat_id = update.effective_message.chat_id
        user= check_if_user_exists(chat_id=chat_id)
        about = update.message.text
        if user:
            edited_user = user.update_about(session=session, about=about)
            update.message.reply_text(f"Your new about is - {edited_user.about}")
            update.message.reply_text("If you want to edit more,Use /editprofile command")        
        return END


def entered_wrong_new_email(update: Update, context: CallbackContext):
    with Session() as session:
        msg = update.message.text
        update.message.reply_text("That doesn't look like an email id. Enter valid email id. (/cancelthis to cancel)")
        return SELECTED_EMAIL


def entered_invalid_phone_no(update: Update, context: CallbackContext):
    with Session() as session:
        update.message.reply_text("That doesn't look like a phone_no. Enter a valid phone_no. (/cancelthis to cancel)")
        return SELECTED_PHONE_NO


def stop_nested(update, context):
    with Session() as session:
        update.message.reply_text('Editing Profile Cancelled')
        return END


def canceledit(update, context):
    update.message.reply_text('Editing Cancelled')
    return END


def timeout_editprofile(update, context):
    with Session() as session:
        update.message.reply_text(
            f'Timeout. Please /editprofile again if you want. (Timeout limit - {editprofile_timeout_time} sec)')
        chat_data = context.chat_data
        chat_data.clear()
        logger.info(f"Timeout for /editprofile")
        return ConversationHandler.END


def wrong_name(update, context):
    update.message.reply_text("Please enter valid name.")
    return NAME


def invalid_phone_no(update, context):
    update.message.reply_text("Please enter valid number.")
    return PHONE_NO


def print_all_tables():
    with Session() as session:
        print([user for user in session.query(User).all()])


def anyrandom(update, context):
    update.message.reply_text('Sorry, I am new to understand this')


def error(update, context):
    logger.warning(f'Update {update} caused an error{context.error}')


if __name__ == '__main__':
    User.__table__.create(engine, checkfirst=True)
    print_all_tables()
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    registration_handler = ConversationHandler(
        entry_points=[CommandHandler('register', register)],
        states={
            NAME: [MessageHandler(Filters.regex(r'^([A-Za-z]*([ ][A-Za-z]+)([ ]?[A-Za-z]+)*)$'), name),
                   MessageHandler(~Filters.regex(r'^([A-Za-z]*([ ][A-Za-z]+)([ ]?[A-Za-z]+)*)$'), wrong_name)],
            GENDER: [CallbackQueryHandler(gender, pattern='^selectmale|selectfemale|selecttrans$')],
            EMAIL_ID: [MessageHandler(Filters.regex(r'^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'), email),
                       MessageHandler(~Filters.regex(r'^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'),
                                      wrong_email)],
            PHONE_NO: [MessageHandler(Filters.regex(r'^[0-9]{10}$'), phone_no),
                       MessageHandler(~Filters.regex(r'^[0-9]{10}$'), invalid_phone_no)],
            ADDRESS: [MessageHandler(Filters.text and ~Filters.command, address)],
            SCHOOL_10th: [MessageHandler(Filters.text and ~Filters.command, school_10th)],
            YEAR_10th: [MessageHandler(Filters.regex('^\d{4}-\d{4}'), year_10th)],
            PERCENT_10th: [MessageHandler(Filters.text and ~Filters.command, percent_10th)],
            SELECTIONCLASS: [CallbackQueryHandler(selectionclass, pattern='^select12th|selectdiploma|selectboth$')],
            BOTH_COMPLETE: [MessageHandler(Filters.text and ~Filters.command, both_complete)],
            COLLEGE_12th: [MessageHandler(Filters.text and ~Filters.command, college_12th)],
            YEAR_12th: [MessageHandler(Filters.regex('^\d{4}-\d{4}'), year_12th)],
            PERCENT_12th: [MessageHandler(Filters.text and ~Filters.command, percent_12th)],
            DIPLOMA_UNIVERSITY_NAME: [MessageHandler(Filters.text and ~Filters.command, diploma_university_name)],
            DIPLOMA_COURCE_NAME: [MessageHandler(Filters.text and ~Filters.command, diploma_cource_name)],
            DIPLOMA_YEAR: [MessageHandler(Filters.regex('^\d{4}-\d{4}'), diploma_year)],
            DIPLOMA_PERCENT: [MessageHandler(Filters.text and ~Filters.command, diploma_percent)],    
            GRADUATION_UNIVERSITY_NAME: [MessageHandler(Filters.text and ~Filters.command, graduation_university_name)],
            GRADUATION_COURCE_NAME: [MessageHandler(Filters.text and ~Filters.command, graduation_cource_name)],
            GRADUATION_YAER: [MessageHandler(Filters.regex('^\d{4}-\d{4}'), graduation_year)],  
            GRADUATION_PERCENT: [MessageHandler(Filters.text and ~Filters.command, graduation_percent)],
            POST_GRADUATION_UNIVERSITY_NAME: [MessageHandler(Filters.text and ~Filters.command, post_graduation_university_name)],
            POST_GRADUATION_COURCE_NAME: [MessageHandler(Filters.text and ~Filters.command, post_graduation_cource_name)],
            POST_GRADUATION_YEAR: [MessageHandler(Filters.regex('^\d{4}-\d{4}'), post_graduation_year)],  
            POST_GRADUATION_PERCENT: [MessageHandler(Filters.text and ~Filters.command, post_graduation_percent)],
            LANGUAGELINK: [CommandHandler('langdone', langdone),
                           MessageHandler(Filters.text and ~Filters.command, lang_link)],
            TECHNICALSKILLS: [CommandHandler('techdone', techdone),
                              MessageHandler(Filters.text and ~Filters.command, technical_skills)],
            PROJECT: [CommandHandler('projectdone', projectdone),
                      MessageHandler(Filters.text and ~Filters.command, projects)],
            ABOUT: [MessageHandler(Filters.text and ~Filters.command, about)],
            RECORD_WORKPHOTO: [CommandHandler('donephotos', donephotos),
                               MessageHandler(Filters.photo, record_workphoto),
                               MessageHandler(Filters.text, no_text_allowed)],
            ConversationHandler.TIMEOUT: [MessageHandler(Filters.text | Filters.command, timeout_register)]

        },
        fallbacks=[CommandHandler('reg_cancel', reg_cancel)],
        conversation_timeout=register_timeout_time
    )

    dp.add_handler(registration_handler)

    edit_data_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(editwhat, pattern='^editname|editemail|editphone|editlanguage|edittechnical_skills|editproject|editabout$')],
        states={
            SELECTED_NAME: [MessageHandler(Filters.text and ~Filters.regex(r'^/cancelthis'), enter_new_name)],
            SELECTED_EMAIL: [
                MessageHandler(Filters.regex(r'^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'), enter_new_email),
                MessageHandler(~Filters.regex(r'^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$') and ~Filters.regex(
                    r'^/cancelthis'), entered_wrong_new_email)],
            SELECTED_PHONE_NO: [MessageHandler(Filters.regex(r'^[0-9]{10}$'), enter_phone_no),
                                MessageHandler(~Filters.regex(r'^[0-9]{10}$') and ~Filters.regex(
                                    r'^/cancelthis'), entered_invalid_phone_no)],
            SELECTED_LANGUAGE: [MessageHandler(Filters.text and ~Filters.regex(r'^/cancelthis'), enter_new_languages)],
            SELECTED_SKILLS: [MessageHandler(Filters.text and ~Filters.regex(r'^/cancelthis'), enter_new_technical_skills)],
            SELECTED_PROJECT: [MessageHandler(Filters.text and ~Filters.regex(r'^/cancelthis'), enter_new_project)],
            SELECTED_ABOUT: [MessageHandler(Filters.text and ~Filters.regex(r'^/cancelthis'), enter_new_about)]

        },
        fallbacks=[CommandHandler('cancelthis', stop_nested)],
        map_to_parent={
            END: END
        }
    )
    editprofile_conv = ConversationHandler(
        entry_points=[CommandHandler('editprofile', editprofile)],
        states={
            SELECTING_ACTION: [edit_data_conv],
        },
        fallbacks=[CommandHandler('canceledit', canceledit)]
    )
    dp.add_handler(editprofile_conv)
    dp.add_error_handler(error)
    dp.add_handler(MessageHandler(Filters.text, anyrandom))

    MODE = os.environ.get("MODE", "polling")
    if MODE == 'webhook':
        SSL_CERT = 'certi/ssl-ctoprofile-tgbot.pem'  # we'll create folder on server and ssl certificate on server itself. no need to create it here. but better to mention here.
        live_server_url = os.environ.get("LIVE_SERVER_URL", "0.0.0.0")
        logger.info('inside WEBHOOK block')
        updater.start_webhook(listen="0.0.0.0", port=8443, url_path=f"{TOKEN}",
                              webhook_url=f"{live_server_url}/{TOKEN}", cert=SSL_CERT)
        logging.info(updater.bot.get_webhook_info())
    else:
        logger.info('inside POLLING block')
        updater.start_polling()
        updater.idle()
