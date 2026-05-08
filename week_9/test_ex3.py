class TestExample:
    def compute(self,x,op):
        if op=="+":
            return x+1
        elif op=="-":
            return x-1
        
    def test_increment(self):
        assert self.compute(5,"+")==6

    def test_decrement(self):
        assert self.compute(7,"-")==8