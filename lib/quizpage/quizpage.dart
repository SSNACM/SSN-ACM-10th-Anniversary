import 'package:cbtapp/resultpage/resultpage.dart';
import 'package:flutter/material.dart';
import 'package:cbtapp/models/topiclist.dart';

class QuizPage extends StatefulWidget {
  @override
  int topicindex;
  QuizPage(this.topicindex);
  _QuizPageState createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  // Define variables to store quiz data
  // List<String> questions = [
  //   'Question 1',
  //   'Question 2',
  //   'Question 3',
  //   'Question 4',
  //   'Question 5',
  // ];
  // List<List<String>> options = [
  //   ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'],
  //   ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'],
  //   ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'],
  //   ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'],
  //   ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'],
  // ];
  // List<List<int>> optionScores = [
  //   [1, 2, 3, 4, 5],
  //   [1, 2, 3, 4, 5],
  //   [1, 2, 3, 4, 5],
  //   [1, 2, 3, 4, 5],
  //   [1, 2, 3, 4, 5],
  // ];
  int currentQuestionIndex = 0;
  int totalScore = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Answer these questions',
          style: TextStyle(
            fontWeight: FontWeight.w700,
            fontSize: 20,
          ),
          textAlign: TextAlign.center,
        ),
        backgroundColor: Color.fromRGBO(64, 75, 96, 0.9),
      ),
      body: Container(
        color: Colors.black,
        alignment: Alignment.topCenter,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Padding(padding: EdgeInsets.all(15)),
            Text(
              topic_list[widget.topicindex].questions[currentQuestionIndex],
              style: TextStyle(fontSize: 24.0, color: Colors.white),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 16.0),
            Column(
              children: topic_list[widget.topicindex]
                  .options
                  .asMap()
                  .entries
                  .map(
                    (entry) => Padding(
                      padding: const EdgeInsets.symmetric(vertical: 8.0),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Color.fromRGBO(64, 75, 96, 0.9),
                          fixedSize: Size(300, 50),
                        ),
                        onPressed: () {
                          setState(() {
                            totalScore += topic_list[widget.topicindex]
                                .optionscores[entry.key];
                            if (currentQuestionIndex <
                                topic_list[widget.topicindex].questions.length -
                                    1) {
                              currentQuestionIndex++;
                            } else {
                              // End of quiz
                              showDialog(
                                context: context,
                                builder: (context) => AlertDialog(
                                  title: Text(
                                    'Quiz complete',
                                    style: TextStyle(color: Colors.white),
                                  ),
                                  backgroundColor:
                                      Color.fromRGBO(64, 75, 96, 0.9),
                                  content: Text(
                                    'Total score: $totalScore',
                                    style: TextStyle(color: Colors.white),
                                  ),
                                  actions: [
                                    TextButton(
                                      onPressed: () {
                                        Navigator.of(context).pop();
                                        setState(() {
                                          currentQuestionIndex = 0;
                                          totalScore = 0;
                                        });
                                      },
                                      child: Text(
                                        'Retry',
                                        style: TextStyle(color: Colors.white),
                                      ),
                                    ),
                                    TextButton(
                                      onPressed: () {
                                        Navigator.push(
                                            context,
                                            MaterialPageRoute(
                                                builder: (context) =>
                                                    ResultPage(totalScore,
                                                        widget.topicindex)));
                                      },
                                      child: Text(
                                        'View Result',
                                        style: TextStyle(color: Colors.white),
                                      ),
                                    ),
                                  ],
                                ),
                              );
                            }
                          });
                        },
                        child: Text(entry.value),
                      ),
                    ),
                  )
                  .toList(),
            ),
          ],
        ),
      ),
    );
  }
}
