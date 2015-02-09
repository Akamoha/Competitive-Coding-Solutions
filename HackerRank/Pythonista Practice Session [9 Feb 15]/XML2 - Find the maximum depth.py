from xml.etree.ElementTree import XMLTreeBuilder
class MaxDepth:                     # The target object of the parser
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
        pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        return self.maxDepth
target = MaxDepth()
parser = XMLTreeBuilder(target=target)
n = int(raw_input())
exampleXml = ""
for _ in range(n):
    exampleXml += raw_input()+"\n"
parser.feed(exampleXml)
print parser.close()-1
