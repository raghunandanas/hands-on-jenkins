from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19708-1381845008-7.gif?__cf_chl_jschl_tk__=b290261be2e3ee500bbf8e86d0fbacb005a0e608-1623982773-0-AV_ONBrx_g7yPAURrfcQXKjkvNE2RN_IQAMLmS_0WJdZ86q6N5o2zHzd3C_fyhXoST36L_opQOGwb9HK8TsdZF1sUyS2dmVyBh6Uomm9SjzjhwaWbt8GEWe7t19lK2uaL-O33vcfXpeFhoHwQ3JGPwyQerJHjuzraD-JcRyj1jpglJ5yMtAIxBoqsI2XwqmIgOx5-awmctczZ1286rPtzS8ynLdwo18Qxof5uuLFpEUY7xWPtgudIzb8QpX9pkz8UYk6wn52WcXLsR-SG0Qb9CblaxhqsLFKnJwF1xknTvgrWUdXVvNgawbsbYiMIS_09qdj47rIYL5BFKpNywcd1AJrC0n2I6icdjIT5AMj-MnPRchzQZ6JZaRjWQtI1kmN_pD0J-XnTVqlQQAj-Y1Q9srwQwXJkws3aezW9kaPqnA5lW8NEHX8oPuO3gB2YtKdb4UOP-MyhcTRIwHBwGcZ9_2pZ_rqxE-Im9pk1SZMqXNY",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19667-1381844937-10.gif",
     "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27162-1381845360-0.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
