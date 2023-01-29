class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        
        ret = []
        for i, ch in enumerate(searchWord):
            candidates = []
            
            for product in products:
                if len(product) < i + 1:
                    continue
                
                if product[i] == ch:
                    candidates.append(product)
                
            
            ret.append(candidates[:3])
            products = candidates
        
        return ret
            
        
        