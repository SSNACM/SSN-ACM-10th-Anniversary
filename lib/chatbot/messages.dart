import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class MessagesScreen extends StatefulWidget {
  final List messages;

  MessagesScreen({Key? key, required this.messages}) : super(key: key);
  launchURL(String url) async {
    if (await canLaunch(url)) {
      await launchURL(url);
    } else {
      throw 'Could not launch $url';
    }
  }

  @override
  _MessagesScreenState createState() => _MessagesScreenState();
}

class _MessagesScreenState extends State<MessagesScreen> {
  ScrollController scrollcontroller = ScrollController();
  @override
  Widget build(BuildContext context) {
    var w = MediaQuery.of(context).size.width;
    return ListView.separated(
      controller: scrollcontroller,
      itemBuilder: (context, index) {
        return Container(
          margin: EdgeInsets.all(10),
          child: Row(
            mainAxisAlignment: widget.messages[index]['isUserMessage']
                ? MainAxisAlignment.end
                : MainAxisAlignment.start,
            children: [
              Container(
                  padding: EdgeInsets.symmetric(vertical: 14, horizontal: 14),
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.only(
                        bottomLeft: Radius.circular(
                          20,
                        ),
                        topRight: Radius.circular(20),
                        bottomRight: Radius.circular(
                            widget.messages[index]['isUserMessage'] ? 0 : 20),
                        topLeft: Radius.circular(
                            widget.messages[index]['isUserMessage'] ? 20 : 0),
                      ),
                      color: widget.messages[index]['isUserMessage']
                          ? Color.fromARGB(255, 14, 129, 171)
                          : Color.fromARGB(255, 15, 159, 206)),
                  constraints: BoxConstraints(maxWidth: w * 2 / 3),
                  child: widget.messages[index]['message'].text.text[0]
                          .contains("https:")
                      ? TextButton(
                          onPressed: () {
                            launch(
                                widget.messages[index]['message'].text.text[0]);
                          },
                          child: Text(
                            "View Catalogue",
                            style: TextStyle(
                              color: Colors.white,
                            ),
                          ))
                      : Text(
                          widget.messages[index]['message'].text.text[0],
                          style: TextStyle(color: Colors.white, fontSize: 16),
                        )),
            ],
          ),
        );
      },
      separatorBuilder: (_, i) => Padding(padding: EdgeInsets.only(top: 10)),
      itemCount: widget.messages.length,
    );
  }
}
