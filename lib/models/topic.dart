class Topic {
  String title;
  List<String> questions;
  Map content;
  List options;
  List<int> optionscores;

  Topic({
    required this.title,
    required this.questions,
    required this.content,
    required this.options,
    required this.optionscores,
  });
}
