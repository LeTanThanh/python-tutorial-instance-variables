from html_document import HtmlDocument

if __name__ == "__main__":
  # Introduction to the Python instance variables

  # from pprint import pprint

  # pprint(HtmlDocument.__dict__)
  # print(type(HtmlDocument.__dict__))  # <class 'mappingproxy'>

  # print(HtmlDocument.version)
  # print(HtmlDocument.extension)

  # html_document = HtmlDocument()
  # print(html_document.__dict__)      # {}
  # print(type(html_document.__dict__)) # <class 'dict'>

  # print(html_document.version)
  # print(html_document.extension)  # 5

  # html_document.version = 6
  # print(html_document.__dict__) # {"version": 6}
  # print(html_document.version)  # 6
  # pprint(HtmlDocument.__dict__)
  # print(HtmlDocument.version)   # 5

  # Initializing instance variables

  blank = HtmlDocument("Blank", "")
  print(blank.__dict__)
  print(blank.name)
  print(blank.contents)
