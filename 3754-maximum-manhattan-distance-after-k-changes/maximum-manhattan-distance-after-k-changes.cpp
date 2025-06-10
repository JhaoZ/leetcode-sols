class Solution {
public:

   int check (string s, char a, char b, int k){

       int pos=0;
       int neg=0;
       int val=0;
       int ans=0;
       for(auto i:s){
           if(i==a || i==b){
               pos++;
               val++;
           }
           else{
               val--;
               neg++;
           }
          // Convert at most k opposite directions to positive
           ans=max(ans,val+2*min(neg,k));
       }

       return ans;

   }

   int maxDistance(string s, int k) {

       int a = check(s,'N','E',k);
       int b = check(s,'N','W',k);
       int c = check(s,'S','E',k);
       int d = check(s,'S','W',k);

       return max({a,b,c,d});
       
       
   }
};