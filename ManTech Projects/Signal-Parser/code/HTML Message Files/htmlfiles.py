

def create_convo1():
    f = open('convo1.html', 'w')

    f.write('''
    <html>
    <link rel="stylesheet" href="styles.css" />
    <body> 
        <div class="wrapper">
            <div class="container">
                <div class="right">
                    <div class="top"><span>To: <span class="name">Intern Project 86 (17039198567)</span></span></div>
                    <div class="chat">
                        <div class="conversation-start">
                            <span>Tuesday, May 14, 2019 4:37 PM</span>
                        </div>
                        <div class="bubble me">
                            Yo
                        </div>
                        <div class="bubble me">
                            This is El-P yo 
                        </div>
                        <div class="bubble me">
                            Ready to drop some mad beats
                        </div>
                        <div class="bubble you">
                            Umm sure 
                        </div>
                        <div class="bubble you">
                            Hippie 
                        </div>
                        <div class="bubble me">
                            Gonna send you something. 
                        </div>
                        <div class="bubble you">
                            Oh noo 
                        </div>
                        <div class="bubble me">
                            this is me as a kid, cool huh 
                        </div>
                        <div class="bubble you">
                            Fresh fruit for yoi 
                        </div>
                        <div class="bubble you">
                            So many comments.  
                        </div>
                        <div class="bubble you">
                            Stupid PG chat  
                        </div>
                        <div class="bubble me">
                            Yeah man, do it for the kids   
                        </div>
                        <div class="bubble me">
                            cow  
                        </div>
                         <div class="bubble me">
                            Wow, we should mix that into a song    
                        </div>
                        <div class="bubble me">
                            chart topper   
                        </div>
                         <div class="bubble you">
                            You are the beat master     
                        </div>
                        <div class="bubble you">
                            I immediately regrett that decision   
                        </div>
                        <div class="bubble me">
                            No can do friendo    
                        </div>
                         <div class="bubble me">
                            PG      
                        </div>
                        <div class="bubble me">
                            hey, we need collaboration with MC PeeWee, let me pull him in here    
                        </div>
                    </div>
                    

                   
                    <div class="write">
                        <a href="javascript:;" class="write-link attach"></a>
                        <input type="text" placeholder="Send a message" />
                        <a href="javascript:;" class="write-link smiley"></a>
                        <a href="javascript:;" class="write-link send"></a>
                    </div>
                </div>
            </div>
        </div>
    <body/>
    </html>
    ''')

    f.close()

def create_convo2():
    f = open('convo2.html', 'w')

    f.write('''
    <html>
    <link rel="stylesheet" href="styles.css" />
    <body> 
        <div class="wrapper">
            <div class="container">
                <div class="right">
                    <div class="top"><span>To: <span class="name">17036516754</span></span></div>
                    <div class="chat">
                        <div class="conversation-start">
                            <span>Tuesday, May 14, 2019 4:38 PM</span>
                        </div>
                        <div class="bubble me">
                            El-P here, add me bro
                        </div>
                        <div class="bubble you">
                            Added  
                        </div>
                    </div>
                    

                   
                    <div class="write">
                        <a href="javascript:;" class="write-link attach"></a>
                        <input type="text" placeholder="Send a message" />
                        <a href="javascript:;" class="write-link smiley"></a>
                        <a href="javascript:;" class="write-link send"></a>
                    </div>
                </div>
            </div>
        </div>
    <body/>
    </html>
    ''')

    f.close()

def create_convo3():
    f = open('convo3.html', 'w')

    f.write('''
    <html>
    <link rel="stylesheet" href="styles.css" />
    <body> 
        <div class="wrapper">
            <div class="container">
                <div class="right">
                    <div class="top"><span>To: <span class="name">El P</span></span></div>
                    <div class="chat">
                        <div class="conversation-start">
                            <span>Tuesday, May 14, 2019 4:35 PM</span>
                        </div>
                        <div class="bubble me">
                            Lunch with Killer Mike on Thursday.
                        </div>
                    </div>
                    

                   
                    <div class="write">
                        <a href="javascript:;" class="write-link attach"></a>
                        <input type="text" placeholder="Send a message" />
                        <a href="javascript:;" class="write-link smiley"></a>
                        <a href="javascript:;" class="write-link send"></a>
                    </div>
                </div>
            </div>
        </div>
    <body/>
    </html>
    ''')

    f.close()

def create_convo4():
    f = open('convo4.html', 'w')

    f.write('''
    <html>
    <link rel="stylesheet" href="styles.css" />
    <body> 
        <div class="wrapper">
            <div class="container">
                <div class="right">
                    <div class="top"><span>To: <span class="name">Intern Project 86, El-P, 17036516754</span></span></div>
                    <div class="chat">
                        <div class="conversation-start">
                            <span>Tuesday, May 14, 2019 4:47 PM</span>
                        </div>
                        <div class="bubble me">
                            Sup Lil' Bo Peep and MC PeeWee 
                        </div>
                        <div class="bubble me">
                            Got a meeting, be back later, El-P out 
                        </div>
                        <div class="bubble you">
                            K. See ya (From: 17036512962)
                        </div>
                    </div>
                    

                   
                    <div class="write">
                        <a href="javascript:;" class="write-link attach"></a>
                        <input type="text" placeholder="Send a message" />
                        <a href="javascript:;" class="write-link smiley"></a>
                        <a href="javascript:;" class="write-link send"></a>
                    </div>
                </div>
            </div>
        </div>
    <body/>
    </html>
    ''')

    f.close()

def create_css():
    f = open('styles.css', 'w')

    f.write('''
    
        @charset "UTF-8";
        *, *:before, *:after {
        box-sizing: border-box;
        }

        :root {
        --white: #fff;
        --black: #000;
        --bg: #f8f8f8;
        --grey: #999;
        --dark: #1a1a1a;
        --light: #e6e6e6;
        --wrapper: 1000px;
        --blue: #00b0ff;
        }

        body {
        background-color: var(--bg);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 400;
        background-size: cover;
        background-repeat: none;
        }

        .wrapper {
        position: relative;
        left: 50%;
        width: var(--wrapper);
        height: 800px;
        transform: translate(-50%, 0);
        }

        .container {
        position: relative;
        top: 50%;
        left: 50%;
        width: 80%;
        height: 75%;
        background-color: var(--white);
        transform: translate(-50%, -50%);
        }
        .container .right {
        position: relative;
        float: left;
        width: 100%;
        height: 100%;
        }
        .container .right .top {
        width: 100%;
        height: 47px;
        padding: 15px 29px;
        background-color: #eceff1;
        }
        .container .right .top span {
        font-size: 15px;
        color: var(--grey);
        }
        .container .right .top span .name {
        color: var(--dark);
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 600;
        }
        .container .right .chat {
        position: relative;
        display: none;
        padding: 0 35px 92px;
        border-width: 1px 1px 1px 0;
        border-style: light;
        border-color: var(--dark);
        height: calc(100% - 48px);
        justify-content: flex-start;
        flex-direction: column;
        overflow-y: auto;
        }
        .container .right .chat {
        display: block;
        display: flex;
        
        }
        .container .right .write {
        position: absolute;
        bottom: 29px;
        left: 30px;
        height: 42px;
        padding-left: 8px;
        border: 1px solid var(--light);
        background-color: #eceff1;
        width: calc(100% - 58px);
        border-radius: 5px;
        }
        .container .right .write input {
        font-size: 16px;
        float: left;
        width: 347px;
        height: 40px;
        padding: 0 10px;
        color: var(--dark);
        border: 0;
        outline: none;
        background-color: #eceff1;
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 400;
        }
        .container .right .write .write-link.attach:before {
        display: inline-block;
        float: left;
        width: 20px;
        height: 42px;
        content: "";
        background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/382994/attachment.png");
        background-repeat: no-repeat;
        background-position: center;
        }
        .container .right .write .write-link.send:before {
        display: inline-block;
        float: right;
        width: 20px;
        height: 42px;
        margin-right: 11px;
        content: "";
        background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/382994/send.png");
        background-repeat: no-repeat;
        background-position: center;
        }
        .container .right .bubble {
        font-size: 16px;
        position: relative;
        display: inline-block;
        clear: both;
        margin-bottom: 8px;
        padding: 13px 14px;
        vertical-align: top;
        border-radius: 5px;
        }
        .container .right .bubble:before {
        position: absolute;
        top: 19px;
        display: block;
        width: 8px;
        height: 6px;
        content: " ";
        transform: rotate(29deg) skew(-35deg);
        }
        .container .right .bubble.you {
        float: left;
        color: var(--white);
        background-color: var(--blue);
        align-self: flex-start;
        -webkit-animation-name: slideFromLeft;
                animation-name: slideFromLeft;
        }
        .container .right .bubble.you:before {
        left: -3px;
        background-color: var(--blue);
        }
        .container .right .bubble.me {
        float: right;
        color: var(--dark);
        background-color: #eceff1;
        align-self: flex-end;
        -webkit-animation-name: slideFromRight;
                animation-name: slideFromRight;
        }
        .container .right .bubble.me:before {
        right: -3px;
        background-color: #eceff1;
        }
        .container .right .conversation-start {
        position: relative;
        width: 100%;
        margin-bottom: 27px;
        text-align: center;
        }
        .container .right .conversation-start span {
        font-size: 14px;
        display: inline-block;
        color: var(--grey);
        }
        .container .right .conversation-start span:before, .container .right .conversation-start span:after {
        position: absolute;
        top: 10px;
        display: inline-block;
        width: 30%;
        height: 1px;
        content: "";
        background-color: var(--light);
        }
        .container .right .conversation-start span:before {
        left: 0;
        }
        .container .right .conversation-start span:after {
        right: 0;
        }

        @keyframes slideFromLeft {
        0% {
            margin-left: -200px;
            opacity: 0;
        }
        100% {
            margin-left: 0;
            opacity: 1;
        }
        }
        @-webkit-keyframes slideFromLeft {
        0% {
            margin-left: -200px;
            opacity: 0;
        }
        100% {
            margin-left: 0;
            opacity: 1;
        }
        }
        @keyframes slideFromRight {
        0% {
            margin-right: -200px;
            opacity: 0;
        }
        100% {
            margin-right: 0;
            opacity: 1;
        }
        }
        @-webkit-keyframes slideFromRight {
        0% {
            margin-right: -200px;
            opacity: 0;
        }
        100% {
            margin-right: 0;
            opacity: 1;
        }
        }

    ''')

    f.close()

create_convo1()
create_convo2()
create_convo3()
create_convo4()
create_css()