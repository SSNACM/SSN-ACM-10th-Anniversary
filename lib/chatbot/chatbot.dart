import 'package:dialog_flowtter/dialog_flowtter.dart';
import 'package:flutter/material.dart';
import 'messages.dart';

void main() => runApp(Chatbot());

class Chatbot extends StatelessWidget {
  const Chatbot({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SieChem',
      theme: ThemeData(brightness: Brightness.light),
      home: Home(),
    );
  }
}

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  late DialogFlowtter dialogFlowtter;
  final TextEditingController _controller = TextEditingController();

  List<Map<String, dynamic>> messages = [];

  @override
  void initState() {
    DialogFlowtter.fromFile().then((instance) => dialogFlowtter = instance);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: Colors.white,
        child: Column(
          children: [
            Card(
              margin: EdgeInsets.all(0),
              elevation: 5,
              child: Container(
                padding: EdgeInsets.all(20),
                child: Text.rich(TextSpan(
                    style:
                        TextStyle(color: Colors.grey[300]), //apply style to all
                    children: [
                      TextSpan(
                          text: '        Hi',
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 28,
                              color: Colors.black)),
                      TextSpan(
                          text:
                              ' I am CBT Bot, you can use the bot to view information about the various therapists available near you..',
                          style: TextStyle(fontSize: 16, color: Colors.black))
                    ])),
                color: Color.fromARGB(255, 236, 233, 233),
                width: double.infinity,
              ),
            ),
            Expanded(child: MessagesScreen(messages: messages)),
            messages.length == 0
                ? Container(
                    height: 60,
                    width: 200,
                    margin: EdgeInsets.only(bottom: 50),
                    child: ElevatedButton(
                      onPressed: () {
                        sendMessage("hello, i need help");
                        _controller.clear();
                      },
                      child: Text("Get Started"),
                      style: ElevatedButton.styleFrom(
                          backgroundColor: Color.fromARGB(255, 15, 159, 206)),
                    ),
                  )
                : Container(
                    decoration: BoxDecoration(
                        borderRadius: BorderRadius.all(Radius.circular(30)),
                        color: Colors.grey[300]),
                    padding: EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                    // color: Colors.purple[100],
                    child: Row(
                      children: [
                        Expanded(
                            child: TextField(
                          controller: _controller,
                          style: TextStyle(color: Colors.black),
                          onSubmitted: (value) {
                            sendMessage(_controller.text);
                            _controller.clear();
                          },
                        )),
                        IconButton(
                            onPressed: () {
                              sendMessage(_controller.text);
                              _controller.clear();
                            },
                            icon: Icon(
                              Icons.send,
                              color: Color.fromARGB(255, 15, 159, 206),
                              size: 30,
                            ))
                      ],
                    ),
                  )
          ],
        ),
      ),
    );
  }

  sendMessage(String text) async {
    if (text.isEmpty) {
      print('Message is empty');
    } else {
      setState(() {
        addMessage(Message(text: DialogText(text: [text])), true);
      });

      DetectIntentResponse response = await dialogFlowtter.detectIntent(
          queryInput: QueryInput(text: TextInput(text: text)));
      if (response.message == null) return;
      setState(() {
        addMessage(response.message!);
      });
    }
  }

  addMessage(Message message, [bool isUserMessage = false]) {
    messages.add({'message': message, 'isUserMessage': isUserMessage});
  }
}
