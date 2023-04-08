import 'package:flutter/material.dart';
import 'package:cbtapp/models/topiclist.dart';

class ResultPage extends StatelessWidget {
  int score;
  int topicindex;
  ResultPage(this.score, this.topicindex);

  @override
  Widget build(BuildContext context) {
    String verdict_text;
    String remedy_text;
    if (score < 25) {
      String verdict_text = topic_list[topicindex].content['low'][0];
      String remedy_text = topic_list[topicindex].content['low'][1];
    } else if (score >= 25 && score <= 50) {
      String verdict_text = topic_list[topicindex].content['moderate'][0];
      String remedy_text = topic_list[topicindex].content['moderate'][1];
    } else {
      String verdict_text = topic_list[topicindex].content['high'][0];
      String remedy_text = topic_list[topicindex].content['high'][1];
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Your Results',
          style: TextStyle(fontWeight: FontWeight.w700, fontSize: 20),
        ),
        backgroundColor: Color.fromRGBO(64, 75, 96, 0.9),
      ),
      body: Container(
        color: Colors.black,
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Card(
              color: Color.fromRGBO(64, 75, 96, 0.9),
              child: Padding(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Verdict',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 24.0,
                      ),
                    ),
                    SizedBox(height: 16.0),
                    Text(
                      "Your interpersonal problems score is low. Your score suggests that you are able to cope effectively in your relationships and build intimate long lasting connections. Your relationships are generally well balanced.",
                      style: TextStyle(fontSize: 20.0, color: Colors.white),
                    ),
                  ],
                ),
              ),
            ),
            SizedBox(height: 16.0),
            Card(
              color: Color.fromRGBO(64, 75, 96, 0.9),
              child: Padding(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Remedy',
                      style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 24.0,
                          color: Colors.white),
                    ),
                    SizedBox(height: 16.0),
                    Text(
                      'You may wish to see a therapist if you have specific concerns that occasionally through you off balance or if you wish to identify certain relationship patterns, more specifically, in order to improve your relationships.',
                      style: TextStyle(fontSize: 20.0, color: Colors.white),
                    ),
                  ],
                ),
              ),
            ),
            Container(
              height: 100,
              padding: EdgeInsets.only(top: 5),
              child: Text(
                "visit a therapist near you!",
                style: TextStyle(color: Colors.white, fontSize: 20),
              ),
              alignment: Alignment.center,
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                  fixedSize: Size(200, 50), backgroundColor: Color(0xff3d2f8d)),
              onPressed: () {},
              child: Text(
                'Search Therapist',
                style: TextStyle(color: Colors.white),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
