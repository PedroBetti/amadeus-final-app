'''
*****************************************************************************************************


███████╗████████╗██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██╗      █████╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██║     ██╔══██╗██╔══██╗██╔════╝
███████╗   ██║   ██████╔╝███████║   ██║   ██║   ██║███████╗    ██║     ███████║██████╔╝███████╗
╚════██║   ██║   ██╔══██╗██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██╔══██║██╔══██╗╚════██║
███████║   ██║   ██║  ██║██║  ██║   ██║   ╚██████╔╝███████║    ███████╗██║  ██║██████╔╝███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝


****************************************************************************************************

*** REDEFINING THE IMPOSSIBLE ***
*** 2020 - 2021 ***

*** Project id : AMADEUS ***
*** Description : Adaptive speech A.I. system using ML/NeuralNet/Tensorflow in Python/Java/HTML5 *** 
*** Researcher : Pedro H.C. Betti ***


****************************************************************************************************
'''

#from chatbot import chatbot
from flask import Flask, render_template , request
from flask import jsonify
import json
from json import dumps
from flask_cors import CORS, cross_origin
from waitress import serve
import random


app = Flask(__name__)
app.static_folder = 'static'

CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins": "*",
        "methods": ["GET", "OPTIONS"]}})


#API ROOT FOLDER
@app.route("/")
def home():
    userText = request.args.get('msg')
    return render_template("index.html")

@app.route("/DescribeEmoji", methods=['GET'])
def Dscription():
    if request.method == 'GET':
        EmojiId = request.args.get('msg')
        EmojiDes = "none"
        desc_id = random.randint(1,3)

        #cookie
        if EmojiId == "1F36A":
            if desc_id == 1:
                EmojiDes = "Famous puppet monster character only eats these!"
            if desc_id == 2:
                EmojiDes = "Who stole one of these from the jar?"
            if desc_id == 3:
                EmojiDes = "Chocolate chips are on this treat!"
        #scissors
        if EmojiId == "2702":
            if desc_id == 1:
                EmojiDes = "Use these to cut up paper!"
            if desc_id == 2:
                EmojiDes = "Don't run with ____s!"
            if desc_id == 3:
                EmojiDes = "Snip Snip!"
        #girraffe
        if EmojiId == "1F992":
            if desc_id == 1:
                EmojiDes = "Long necked african animal!"
            if desc_id == 2:
                EmojiDes = "Yellow animal with spots!"
            if desc_id == 3:
                EmojiDes = "This can get food from the highest branches!"
        #burger
        if EmojiId == "1F354":
            if desc_id == 1:
                EmojiDes = "Americas favourite food!"
            if desc_id == 2:
                EmojiDes = "Lettuce, Tomato, Onions, Ketchup, Mustard???"
            if desc_id == 3:
                EmojiDes = "The crabby patty is a ____!"
        #flashlight
        if EmojiId == "1F526":
            if desc_id == 1:
                EmojiDes = "Shine light on something with this handy tool!"
            if desc_id == 2:
                EmojiDes = "In the UK they call this a 'torch'"
            if desc_id == 3:
                EmojiDes = "In a dark cave you need this item."
        #balloon
        if EmojiId == "1F388":
            if desc_id == 1:
                EmojiDes = "Its not a party without several colored ____s!"
            if desc_id == 2:
                EmojiDes = "Poke it with a needle and It'll pop!"
            if desc_id == 3:
                EmojiDes = "These things float away if you dont hold them."
        #baseball
        if EmojiId == "26BE":
            if desc_id == 1:
                EmojiDes = "This ball gets hit by a bat!"
            if desc_id == 2:
                EmojiDes = "Worlds most boring sports ball"
            if desc_id == 3:
                EmojiDes = "Run from base to base after you hit this object!"
        #televission
        if EmojiId == "1F4FA":
            if desc_id == 1:
                EmojiDes = "I use this to experience other places from the comfort of my own home!"
            if desc_id == 2:
                EmojiDes = "Satelite or Cable?"
            if desc_id == 3:
                EmojiDes = "Where can I watch Game of Thrones?"
        #piano
        if EmojiId == "1F3B9":
            if desc_id == 1:
                EmojiDes = "This instrument has many notes!"
            if desc_id == 2:
                EmojiDes = "There's a 'Grand' version."
            if desc_id == 3:
                EmojiDes = "Make sounds with your fingers!"
        #teddybear
        if EmojiId == "1F9F8":
            if desc_id == 1:
                EmojiDes = "childs fluffy friendly toy"
            if desc_id == 2:
                EmojiDes = "there are many kinds of this creature, polar, black and stuffed"
            if desc_id == 3:
                EmojiDes = "a toy made in the image of a savage, big, wild creature"
        #chicken
        if EmojiId == "1F414":
            if desc_id == 1:
                EmojiDes = "you can eat this bird many ways, rosted, grilled, or fried"
            if desc_id == 2:
                EmojiDes = "KFC is famous for making fried dishes with this"
            if desc_id == 3:
                EmojiDes = "when you are not brave you are a "
        #eagle
        if EmojiId == "1F985":
            if desc_id == 1:
                EmojiDes = "American bald and endangered animal"
            if desc_id == 2:
                EmojiDes = "this animal likes to eat fish, and hunts at great heights"
            if desc_id == 3:
                EmojiDes = "A symbol of the roman imperial legion"
        #skull
        if EmojiId == "1F480":
            if desc_id == 1:
                EmojiDes = "the top most part of a very bony individual"
            if desc_id == 2:
                EmojiDes = "shakespere talks to one"
            if desc_id == 3:
                EmojiDes = "pirate flew flags with this on their symbol"
        #book
        if EmojiId == "1F4D5":
            if desc_id == 1:
                EmojiDes = "a library carries these in abundance"
            if desc_id == 2:
                EmojiDes = "paperback or hardcover"
            if desc_id == 3:
                EmojiDes = "dont judge it by its cover"
        #yarn
        if EmojiId == "1F9F6":
            if desc_id == 1:
                EmojiDes = "used by grandmothers to make sweathers"
            if desc_id == 2:
                EmojiDes = "a fan favorite of kittens"
            if desc_id == 3:
                EmojiDes = "this red thing led theseus through the minotaurs labyrinth"
        #key
        if EmojiId == "1F511":
            if desc_id == 1:
                EmojiDes = "a method for locking and unlocking secure items"
            if desc_id == 2:
                EmojiDes = "the mystery door needs a key"
            if desc_id == 3:
                EmojiDes = "another word for kilograms"
        #umbrella
        if EmojiId == "26F1":
            if desc_id == 1:
                EmojiDes = "favorite item of a certain magical maid"
            if desc_id == 2:
                EmojiDes = "name of a certain research organization that owns raccoon city"
            if desc_id == 3:
                EmojiDes = "used frequently for protection against the elements"
        #bow
        if EmojiId == "1F3F9":
            if desc_id == 1:
                EmojiDes = "a notable english thief likes this weapon"
            if desc_id == 2:
                EmojiDes = "this is a weapon used by classes like rangers and ranged units in rpgs"
            if desc_id == 3:
                EmojiDes = "used for silent hunting"
        #axe
        if EmojiId == "1FA93":
            if desc_id == 1:
                EmojiDes = "a brutes favortie weapon"
            if desc_id == 2:
                EmojiDes = "a blashmith would carry this tool"
            if desc_id == 3:
                EmojiDes = "used to cut wood for fires"
        #pig
        if EmojiId == "1F437":
            if desc_id == 1:
                EmojiDes = "baccon is one of the things this creature is known for"
            if desc_id == 2:
                EmojiDes = "pepa the "
            if desc_id == 3:
                EmojiDes = "Kermit the muppet fell in love with miss"
        #candle
        if EmojiId == "1F56F":
            if desc_id == 1:
                EmojiDes = "shrek makes these with ease"
            if desc_id == 2:
                EmojiDes = "a romantic dinner is not complete without these"
            if desc_id == 3:
                EmojiDes = "a medieval ligthing device"



        return jsonify({'EmojiId': EmojiId, "EmojiDescription": EmojiDes})

    

@app.route("/ClassifyEmoji" , methods=['GET'])
def Classification():

    if request.method == 'GET':
        Descript = request.args.get('msg')
        #emoji id comes from NN guess [ 1 - 7 ]
        E_ID = "00000"
        E_name = "unknown"

        cookie_keyword_list = [["cookie","cookies","chocolate","chips","crumb","desert","flour","homemade"],
                           ["home","food","made","biscuit","sugar","rasin","fourtune","gingersnap","giner","bake"],
                           ["baking","dough","batter","lick","favourite","famous","hot","warm","round","circle"],
                           ["fresh","treat","brown","classic","oreo","oreos","monster","sesame","street","mom","mother"], ]
        scissors_keyword_list = [["scissors","scissor","cut","bladed","cutting","paper","sharp","rock"],
                           ["curved","fine","surgical","knife","saw","shred","construction","children","tool","slash"],
                           ["dont run","don't run","with","loop","grip","plastic","meatal","quality","arent sharp","two blades"],
                           ["stab","pierce","gash","weapon","plural","rusty"] ]
        balloon_keyword_list = [["balloon","baloon","hot","air","party","parties","celebration","celebrations"],
                           ["clown","clowns","red","colour","colours","bag","cheap","event","special","fly"],
                           ["soar","air","sky","helium","atmosphere","pop","poppy","loud"],
                           ["sound","noise","gas","vechile","transportation"] ]
        basebal_keyword_list = [["bat","baseball","sports","base","home","throw","hurl","throws","spin","ball"],
                           ["first","second","third","run","white","homerun","leather","stitch","stitches","stitching"],
                           ["hit","loud","crowd","sport","television","tv","mlb","blue jays","blue","jays"],
                           ["pitcher","pitch","curve","ball","strike","shortstop","catcher","field","out","park","fastball","major","league","tripple","single","double","pro","professional","american","boring"] ]
        burger_keyword_list = [["burger","hamburger","cheese","lettuce","mustard","ketchup","food","mayo","mayonnaise","meat"],
                           ["patty","pickles","pickle","tomato","onion","bun","eat","fries","fry","with fries"],
                           ["common","famous","popular","meat","cow","hungry","filling","calorie","calories","seed"],
                           ["america","american","western","hamburg","mcdonalds","vegeterian","harveys","a&w","fast food","service","drive through"] ]
        tv_keyword_list = [["tv","television","show","movie","channel","antenna","broadcast","favourite","game","tuner"],
                           ["network","movies","theatre","netflix","remote","cable","satellite","internet","news","sports"],
                           ["box","resolution","screen","commercials","commercial","national","american","digital","live","display"],
                           ["living","room","image","pixels","movie","transmit","wave","waves","receiver","views","remote control","control","knob","time","buttons","side","breaking bad","walking dead","game of thrones","the office","celebrity","violence","sex"] ]
        flashlight_keyword_list = [["flashlight","light","flash","flash light","lamp","torch","battery","woods","dark","night"],
                           ["shine","head","mount","candle","cave","click","button","hold hand","scary","scared"],
                           ["shine","head","mount","candle","cave","click","button","hold hand","scary","scared"],
                           ["camp","tent","photons","flash"] ]
        griraffe_keyword_list = [["giraffe","girafe","africa","african","big","long","long neck","tall","neck","necked","yellow","spot"],
                           ["animal","large","spotted","sky","air","high","lift","up","alive","living"],
                           ["lion","herbivore","creature","four legs"],
                           ["run","horn","horns","trees","tree"] ]
        piano_keyword_list = [["piano","key","instrument","keys","black","keyboard","electric","keyboards","white","song"],
                           ["music","chords","chord","big","chopsticks","classical","yamaha","grand","steinway","pedal"],
                           ["sustain","expression","acoustic","pianist","play","sit","stool","fingers","ballad","moving"],
                           ["heavy","pop","radio","melody","theory","music theory","rcm","royal","conservatory"] ]
        chicken_keyword_list = [["chicken","fried","cold","little","roast", "fried","whole","chicken","grilled","roasted","bird"],
                           ["young","cooked","live","broiled","boiled","dead","white","domestic","baked","raw","pound"],
                           ["plucked","fresh","fat","barbecued","hot","delicious","spicy","plump","wild","crispy"],
                           ["cluck","clucked","beak","feather","kfc","mcdonalds","mc","donalds"] ]
        teddybear_keyword_list = [["black","fluff","friendly","friend","animal","ferocious","creature","fluffy","full","hair"],
                           ["happy","polar","grizzly","brown","cuddly","big","old","little","great","white","large"],
                           ["huge","teddy","stuffed","wild","bear","brown","grizzly","shaggy","giant","little","girl"],
                           ["grisly","woolly","fierce","savage"] ]
        eagle_keyword_list = [["bald","wing","wings","bird","claws","endangered","wild","fly","sky","soar","beak"],
                           ["mice","catch","predator","animal","creature","wind","feather","golden","american","headed","great"],
                           ["black","imperial","white","harpy","winged","lone","bronze"],
                           ["caged","wingspan","white","black","majestic","claw"] ]
        skull_keyword_list = [["human","fractured","thick","fossil","bony","dig","dead","skull","crossbones","pirate","teeth"],
                           ["human","head","dry","broken","cracked","crushed","shattered","bone","bones","dog","eye"],
                           ["holes","dirt","earth","ground"],
                           ["teeth","face","nose","assasins creed"] ]
        book_keyword_list = [["first","little","comic","book","hardcover","author","readable","read","write","page","number"],
                           ["intelligent","Catcher","bible","story","read","book","novel","binder","year","famous","famous"],
                           ["Rings","Harry Potter","Quixote","Mockingbird","Gatsby","new","second","whole","present","recent","text"],
                           [ "last","entire","third","excellent","best","open","interesting","fourth","note","hand","smart","library","useful","library","school","teacher","apple"] ]
        yarn_keyword_list = [["yarn","ball","bounce","red","knit","colored","long","string","cat","kitty", "kittens","play"],
                           ["fun","clothes","soft","made","make","needle","needles","cotton","smooth","textured","linen"],
                           ["light","feline","twisted","spun","knot","tangle"],
                           ["tangled","loose","knots","dyed","knitting","sweater"] ]
        key_keyword_list = [["primary","door","lock","safe","secure","security","password","get in","safe","criminal","steal"],
                           ["protection","safe","guard","secret","rigged","bump","combination","golden","yellow","gold","tool"],
                           ["home","building","expensive","value","valuable","special","keyhole","original","shared","room","flat"],
                           ["important","fundamental","central","kilogram","significant","name","harmonise","harmonize","list","listing","passkey","latchkey","lock","major key","minor key","tab key","provide","keyboard","space bar","vandalize","tab","winder","distinguish","discover","describe","primal","cay","cardinal","tonality","identify","keystone","shift key","control key","key word","backspace","door","command key","key out","kg","kilo","crucial","major","leading","main","top","of import","one","critical","strategy","priority","pressing","pivotal","master key"] ]
        umbrella_keyword_list = [["umbrella","big","rain","rainy","weather","wet","curve","dome","shape","handle","cane"],
                           ["marry","poppins", "raccoon city", "raccoon", "city","black","color","dark","somber","remember","forget","inflate","indoors","wide"],
                           ["catch","water","canopy","shade","union","defense","comprehensive","tent","defence","brolly","organization"],
                           ["rain","alliance","grouping","priest","offshoot","rainbow","splinter","heads","advocacy","parasol","cloak","associations","entity","banner","storm","awning","tool","precipitation","sunburn","blanket","drape","parachute","umbel","slang","uniting","unification","jointure","rib"] ]
        bow_keyword_list = [["bow","weapon","arrow","bow and arrow","archery","weapon","crossbow","longbow","archer","robin","robinhood","leather"],
                           ["cap","string","rope","stick","flint","tool","primitive","target","sport","accuracy","whirl", "theif", "ranger", "dnd", "dungeon dragons", "dungeon", "dragons"],
                           ["air","fast","speed","power","hand","hand held"],
                           [ "ammo","stick","william","tell","william tell"] ]
        axe_keyword_list = [["axe","hatchet","blade","chop","hand axe","steel","hammer","wood","chop","lumber","jack"],
                           ["lumberjack","red","brown","stick","handle","sharp","tree","trees","fall","tool","broadaxe"],
                           ["edge","tool","knife","machete","sword","bladed","hilt","scythe","hacksaw","scabbard","tomahawk"],
                           ["neolithic","millennium","harvest","lumber","ceremony","heraldry","symbol","hack","end","handle","rock","copper","bronze","iron","razor","sticks","firefighter","zombie"] ]
        pig_keyword_list = [["pig","pigs","pink","curly","tail","fat","farm","mud","play","animal","bacon"],
                           ["pork","smart","red","light","snout","nose","live","alive","fatty","faty","living","kermit","muppets"],
                           ["ears","creature","bacon","swine","dig","cow","fence","domestic","domesticated","eggs","livestock"],
                           ["covered","guinea","dead","roast","sizzle","pop","grease"] ]
        candle_keyword_list = [["candle","candles","light","drip","shine","fire","flame","burn","stick","scented","gift"],
                            ["tall","bright","dark","wic","electricity","burn","flicker","run out","dim","bulb","time"],
                           ["candela","taper","lamp","fire","light","wax","flame","candlewick","candlelight","lantern","candlestick","shrek","romantic"],
                           ["candle wick","beeswax","pyre","spermaceti","menorah","torch","celebration","fireplace","lights","bulb","wreath","firelight","flashlight","candlepower","kerosene","lightbulb","paraffin wax","heat","time","incandescent","string","dip","wick","oxygen","rope","candle clock","chandler","flickering","lighted","chimes","lamps","neon","house","lanterns","glass","scented","bonfires","glow","crate"] ]
 
        search = Descript
        
        num0 = 0
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        num5 = 0
        num6 = 0
        num7 = 0
        num8 = 0
        num9 = 0
        num10 = 0
        num11 = 0
        num12 = 0
        num13 = 0
        num14 = 0
        num15 = 0
        num16 = 0
        num17 = 0
        num18 = 0
        num19 = 0
        num20 = 0
        num21 = 0

        for sublist in  cookie_keyword_list:
            if sublist[0] in search:
                num1 += 4
            if sublist[1] in search:
                num1 += 3
            if sublist[2] in search:
                num1 += 2
            if sublist[3] in search:
                num1 += 1

        for sublist in scissors_keyword_list:
            if sublist[0] in search:
                num2 += 4
            if sublist[1] in search:
                num2 += 3
            if sublist[2] in search:
                num2 += 2
            if sublist[3] in search:
                num2 += 1

        for sublist in balloon_keyword_list:
            if sublist[0] in search:
                num3 += 4
            if sublist[1] in search:
                num3 += 3
            if sublist[2] in search:
                num3 += 2
            if sublist[3] in search:
                num3 += 1
        
        for sublist in basebal_keyword_list:
            if sublist[0] in search:
                num4 += 4
            if sublist[1] in search:
                num4 += 3
            if sublist[2] in search:
                num4 += 2
            if sublist[3] in search:
                num4 += 1
        
        for sublist in burger_keyword_list:
            if sublist[0] in search:
                num5 += 4
            if sublist[1] in search:
                num5 += 3
            if sublist[2] in search:
                num5 += 2
            if sublist[3] in search:
                num5 += 1
        
        for sublist in tv_keyword_list:
            if sublist[0] in search:
                num6 += 4
            if sublist[1] in search:
                num6 += 3
            if sublist[2] in search:
                num6 += 2
            if sublist[3] in search:
                num6 += 1
        
        for sublist in flashlight_keyword_list:
            if sublist[0] in search:
                num7 += 4
            if sublist[1] in search:
                num7 += 3
            if sublist[2] in search:
                num7 += 2
            if sublist[3] in search:
                num7 += 1

        for sublist in griraffe_keyword_list:
            if sublist[0] in search:
                num8 += 4
            if sublist[1] in search:
                num8 += 3
            if sublist[2] in search:
                num8 += 2
            if sublist[3] in search:
                num8 += 1

        for sublist in piano_keyword_list:
            if sublist[0] in search:
                num9 += 4
            if sublist[1] in search:
                num9 += 3
            if sublist[2] in search:
                num9 += 2
            if sublist[3] in search:
                num9 += 1
        
        for sublist in chicken_keyword_list:
            if sublist[0] in search:
                num10 += 4
            if sublist[1] in search:
                num10 += 3
            if sublist[2] in search:
                num10 += 2
            if sublist[3] in search:
                num10 += 1
        
        for sublist in teddybear_keyword_list:
            if sublist[0] in search:
                num11 += 4
            if sublist[1] in search:
                num11 += 3
            if sublist[2] in search:
                num11 += 2
            if sublist[3] in search:
                num11 += 1
        
        for sublist in eagle_keyword_list:
            if sublist[0] in search:
                num12 += 4
            if sublist[1] in search:
                num12 += 3
            if sublist[2] in search:
                num12 += 2
            if sublist[3] in search:
                num12 += 1

        for sublist in skull_keyword_list:
            if sublist[0] in search:
                num13 += 4
            if sublist[1] in search:
                num13 += 3
            if sublist[2] in search:
                num13 += 2
            if sublist[3] in search:
               num13 += 1
        
        for sublist in book_keyword_list:
            if sublist[0] in search:
                num14 += 4
            if sublist[1] in search:
                num14 += 3
            if sublist[2] in search:
                num14 += 2
            if sublist[3] in search:
                num14 += 1

        for sublist in yarn_keyword_list:
            if sublist[0] in search:
                num15 += 4
            if sublist[1] in search:
                num15 += 3
            if sublist[2] in search:
                num15 += 2
            if sublist[3] in search:
                num15 += 1

        for sublist in key_keyword_list:
            if sublist[0] in search:
                num16 += 4
            if sublist[1] in search:
                num16 += 3
            if sublist[2] in search:
                num16 += 2
            if sublist[3] in search:
                num16 += 1
            
        for sublist in umbrella_keyword_list:
            if sublist[0] in search:
                num17 += 4
            if sublist[1] in search:
                num17 += 3
            if sublist[2] in search:
                num17 += 2
            if sublist[3] in search:
                num17 += 1

        for sublist in bow_keyword_list:
            if sublist[0] in search:
                num18 += 4
            if sublist[1] in search:
                num18 += 3
            if sublist[2] in search:
                num18 += 2
            if sublist[3] in search:
                num18 += 1

        for sublist in axe_keyword_list:
            if sublist[0] in search:
                num19 += 4
            if sublist[1] in search:
                num19 += 3
            if sublist[2] in search:
                num19 += 2
            if sublist[3] in search:
                num19 += 1

        for sublist in pig_keyword_list:
            if sublist[0] in search:
                num20 += 4
            if sublist[1] in search:
                num20 += 3
            if sublist[2] in search:
                num20 += 2
            if sublist[3] in search:
                num20 += 1

        for sublist in candle_keyword_list:
            if sublist[0] in search:
                num21 += 4
            if sublist[1] in search:
                num21 += 3
            if sublist[2] in search:
                num21 += 2
            if sublist[3] in search:
                num21 += 1

        print( num1," ",num2," ",num3," ",num4," ",num5," ",num6," ",num7," ",num8," ",num9," ",num10," ",num11," ",num12," ",num13," ",num14," ",num15," ",num16," ",num17," ",num18," ",num19," ",num20," ",num21)
        if ((num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20,num21) == 0):
            num0 += 4

        data = {"0" : num0,
                "1" : num1,
                "2" : num2,
                "3" : num3,
                "4" : num4,
                "5" : num5,
                "6" : num6,
                "7" : num7,
                "8" : num8,
                "9" : num9,
                "10" : num10,
                "11" : num11,
                "12" : num12,
                "13" : num13,
                "14" : num14,
                "15" : num15,
                "16" : num16,
                "17" : num17,
                "18" : num18,
                "19" : num19,
                "20" : num20,
                "21" : num21}
        print (max(data, key=data.get))

        if (max(data, key=data.get) == "0"):
            E_ID = "00000"
            E_name = "unknown"
        if (max(data, key=data.get) == "1"):
            E_ID = "1F36A"
            E_name = "Cookie"
        if (max(data, key=data.get) == "2"):
            E_ID = "2702"
            E_name = "Scissors"
        if (max(data, key=data.get) == "3"):
            E_ID = "1F388"
            E_name = "Balloon"
        if (max(data, key=data.get) == "4"):
            E_ID = "26BE"
            E_name = "Baseball"
        if (max(data, key=data.get) == "5"):
            E_ID = "1F354"
            E_name = "Burger"
        if (max(data, key=data.get) == "6"):
            E_ID = "1F4FA"
            E_name = "Television"
        if (max(data, key=data.get) == "7"):
            E_ID = "1F526"
            E_name = "Flashlight"
        if (max(data, key=data.get) == "8"):
            E_ID = "1F992"
            E_name = "Giraffe"
        if (max(data, key=data.get) == "9"):
            E_ID = "1F3B9"
            E_name = "Piano"
        if (max(data, key=data.get) == "10"):
            E_ID = "1F414"
            E_name = "chicken"
        if (max(data, key=data.get) == "11"):
            E_ID = "1F9F8"
            E_name = "TeddyBear"
        if (max(data, key=data.get) == "12"):
            E_ID = "1F985"
            E_name = "Eagle"
        if (max(data, key=data.get) == "13"):
            E_ID = "1F480"
            E_name = "Skull"
        if (max(data, key=data.get) == "14"): 
            E_ID = "1F4D5"
            E_name = "Book"
        if (max(data, key=data.get) == "15"):
            E_ID = "1F9F6"
            E_name = "Yarn"
        if (max(data, key=data.get) == "16"):
            E_ID = "1F511"
            E_name = "Key"
        if (max(data, key=data.get) == "17"):
            E_ID = "26F1"
            E_name = "Umbrella"
        if (max(data, key=data.get) == "18"):
            E_ID = "1F3F9"
            E_name = "Bow and Arrow"
        if (max(data, key=data.get) == "19"):
            E_ID = "1FA93"
            E_name = "Axe"
        if (max(data, key=data.get) == "20"):
            E_ID = "1F437"
            E_name = "Pig"
        if (max(data, key=data.get) == "21"):
            E_ID = "1F56F"
            E_name = "Candle"
        

        data_game = {}
        data_game = {
            "Description": Descript ,
            "Emoji_ID": E_ID ,
            "Emoji_Name": E_name
        }

        json_data = json.dumps(data_game)
        print(json_data)
        return json_data

#RESPONSE API
@app.route("/get_bot_response" , methods=[ 'GET'])
def get_bot_response():
    if request.method == 'GET':
        userText = request.args.get('msg') 
        response = str(chatbot.get_response(userText))

    ##PATCH VER JAN 08 2021 
        #INTENT SEARCH 
        s = userText
        intent = 'normal conversation'

        #INTENT CLASSIFICATION
        ##(FIND OTHER KEY WORDS AND CONVERSATIONAL MATERIAL)
        ###(SHOULD BE REPLACED WITH ML MODEL FOR FINDING INTENT IN [S])
        g = s.find("Hello")
        g = s.find("hello")
        g = s.find("Hi")
        g = s.find("hi")
        h = s.find("Cats")
        h = s.find("cats")
        a = s.find('Fuck you')
        a = s.find('fuck you')

        if g!= -1:
            intent = 'greeting' 
        if h!= -1:
            intent = 'happy'
        if a!= -1:
            intent = 'anger'
 
        #RESPONSE & INTENT JSON CONVERSION
        data_conv ={}
        data_conv = {
            "botResponse": response ,
            "intent": intent
        }
    ##PATCH VER JAN 08 2021 --END-- 

        #YML FILE WRITER
        with open ("test1.yml" , 'a') as f:
            f.write("\n")
            f.write("- - ")
            f.write(userText)
            f.write("\n")
            f.write("  - ")
            f.write(response)
            
    ##PATCH VER JAN 08 2021       
        #JSON CONVERSION FINALIZATION
        json_convo = json.dumps(data_conv)
        #json_int = json.dumps(data_int)

    #FOR OCAD PROFS WHO NEED TO SEE PRETTY PICTURES AND DONT UNDERSTAND CODE ALMOST AT ALL
        print("USER : "+userText)
        print("RESPONSE : "+response)
        print(json_convo)
    
        #RETURNS JSON OBJECTS & ORIGNAL RESPONSE
        return response + json_convo
    ##PATCH VER JAN 08 2021 --END--   

#QUESTION API
@app.route("/get_bot_question" , methods=[ 'GET'])
def get_bot_question():
    if request.method == 'GET':
        qustText = request.args.get('qus')
        question = str(chatbot.get_response(qustText))
        print(question)
        return question


#API SETTINGS
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=8080) 