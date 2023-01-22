import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m4wmgweb.json")
lottie_coding1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qxmkn9ou.json")
lottie_coding2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_mn0yeqfs.json")
lottie_coding3 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
    

selected = option_menu(None, ["Home", "How to use", "Analyze", 'Contact Us'], 
    icons=['house', 'question-circle', "twitter", 'envelope'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Home":
    st.title("Twitter Sentiment Analysis")
    st.subheader("Hey there!!! :wave: Welcome to our service")
    
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Wondering what we do?")
            st.markdown("We **_analyze_** the tweets for you guys to")
            st.write("1. Clear your doubts\n 2. Authenticity of rumors\n 3. Give you a topic for your gossips\n 4. Help in your philosophical research\n and much more!!!")
            st.write("Go to the Analyze tab to see the magic:sparkles::sparkles:")
        with right_column:
            st_lottie(lottie_coding3, height=400, key="coding")
     
    with st.container():
        st.subheader("How?!")
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown('<div style="text-align: justify;">We use a sentiment analysis technique which is very popular in the world of Machine Learning and Natural Language Processing (NLP). Sentiment analysis refers to identifying as well as classifying the sentiments that are expressed in the text source. Tweets are often useful in generating a vast amount of sentiment data upon analysis. These data are useful in understanding the opinion of the people about a variety of topics. Therefore we developed an Automated Machine Learning Sentiment Analysis Model in order to compute the customer perception.</div>', unsafe_allow_html=True)
            st.write("\n")
            st.markdown('<div style="text-align: justify;">Twitter sentiment analysis allows you to keep track of what is being said about your product or service on social media, and can help you detect angry customers or negative mentions before they they escalate. At the same time, Twitter sentiment analysis can provide valuable insights that drive decisions.</div>', unsafe_allow_html=True)
            st.write("\n")
            st.write("\n")
            st.write("\n")
           
    with st.container():
        st.subheader("Implementation")
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown('<div style="text-align: justify;">We attempted to do some basic NLP techniques using TextBlob library. The tweets are being extracted using the twitter API named tweepy. After the extracting the dataset we do some pre-processing like stemming, tokenizing, etc. After that we use the inbuilt Naive Bayes model to classify the tweets and display the our analysis to you guys through data visualization.</div>', unsafe_allow_html=True)
            st.write("\n")
            st.write("Here is an instance to show you guys the accuracy of our model")
            image6 = Image.open('img/image6.png')
            st.image(image6)
            
if selected == "How to use":
    with st.container():
        left_col, middle_col, right_col = st.columns(3)
        with middle_col:
            st_lottie(lottie_coding2, height=300, key="coding")
    
    with st.container():
        st.title("Didn't know how to use?!")
        st.subheader("No need to worry, it's very simple")
        st.write("Just follow the steps listed below:-")
        st.write("1. Firstly, go to the 'Analyze' tab.")
        image = Image.open('img/image.png')
        st.image(image)
        st.write("\n")
        st.write("2. There are three options available as shown in the figure")
        image1 = Image.open('img/image1.png')
        st.image(image1)
        st.write("\n")
        st.write(" The three options listed are for different types of users :-")
        st.write("-> First option is for the purpose if you want to analyze the tweets of a particular twitter account")
        st.write("-> Second option is used, if you want analyze the tweets for a particular topic or a hashtag")
        st.write("-> Third option is for the users who have their own dataset of tweets and want to analyze only that tweets")
        st.write("\n")
        st.write("3. Select the appropriate option and click on the highlighted area 'Click Here >'")
        image2 = Image.open('img/image2.png')
        st.image(image2)
        st.write("\n")
        st.write("4. Now each option has it's own window")
        st.write("-> Window under first option is shown below :-")
        image3 = Image.open('img/image3.png')
        st.image(image3)
        st.write("(i) Enter the username of the account")
        st.write("(ii) Enter the number of tweets")
        st.write("(iii) Click on 'Get Tweets'")
        st.write("\n")
        st.write("-> Window under second option is shown below :-")
        image4 = Image.open('img/image4.png')
        st.image(image4)
        st.write("(i) Enter the keyword")
        st.write("(ii) Enter the number of tweets")
        st.write("(iii) Click on 'Get Tweets'")
        st.write("\n")
        st.write("-> Window under third option is shown below :-")
        image5 = Image.open('img/image5.png')
        st.image(image5)
        st.write("(i) Upload the .csv file of your dataset")
        st.write("(ii) Enter the name of the column containing the tweets in your dataset")
        st.write("(iii) Click on 'Get Tweets'")
        st.write("\n")
        st.write("After clicking on Get Tweets in each of the option you will get the visualization for our analysis")

if selected == "Analyze":
    st.title("Let's get started")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            genre = st.radio("What do you want to do",
                             ('I want to analyze the tweets from a twitter account', 'I want to analyze a topic', 'I want to analyze my dataset'))

            if genre == "I want to analyze the tweets from a twitter account":
                st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-1.streamlit.app/)")

            if genre == "I want to analyze a topic":
                st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-3.streamlit.app/)")

            if genre == "I want to analyze my dataset":
                st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-2.streamlit.app/)")
            
        with right_column:
            st_lottie(lottie_coding, height=250, key="coding")
        
    with st.container():
        st.subheader("Before going further please read the following instruction :-")
        st.write("1. Maximum 10 tweets will be displayed due to the data and privacy protection bill")
        st.write("2. Tweets extraction phase may take some time if number of tweets is large")
        st.write("3. The analysis is done purely on the basis of some mathematical computation and we aren't responsible for the results")
        st.write("4. Although it is a result of mathematical coputations but we assure that the results are accurate")
        st.write("5. We are not intended to target any particular group of people, relegion, culture etc. and not intended to hurt anybody's feelings")

if selected == "Contact Us":
#     Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")
    with st.container():
        left_column, right_column = st.columns(2)
        with right_column:
            st_lottie(lottie_coding1, height=550, key="coding")
        with left_column:
            st.write("---")
            st.header("Get In Touch With Us!")
            st.subheader("Feel free to ask anything")

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/kbansal_be20@thapar.edu" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
#             left_column, right_column = st.columns(2)
#             with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
#             with right_column:
            st.empty()

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;'>Team 404 FOUND</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
