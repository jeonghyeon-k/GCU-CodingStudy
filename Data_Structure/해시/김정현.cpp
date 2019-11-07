// reference: https://twpower.github.io/91-how-to-use-map-in-cpp

#include<iostream>
#include<map>
#include<string>

using namespace std;

int main(){
    
    map<string, int> m;
    
    m.insert(make_pair("a",1));
    m.insert(make_pair("a",2));
    m.insert(make_pair("a",3));
    
    m.insert(make_pair("b",4));
    m.insert(make_pair("b",5));
    m.insert(make_pair("b",6));
    
    m.insert(make_pair("c",7));
    m.insert(make_pair("c",8));
    m.insert(make_pair("c",9));
    m["f"] = 10;
    
    // empty(), size()
    if(!m.empty()) cout << "m size : " << m.size() << '\n';
    
    
    // find(key)
    cout << "a : " << m.find("a")->second << '\n';
    cout << "b : " << m.find("b")->second << '\n';
    cout << "c : " << m.find("c")->second << '\n';
    
    
    // count(key)
    cout << "a count : " << m.count("a") << '\n';
    cout << "b count : " << m.count("b") << '\n';
    cout << "c count : " << m.count("c") << '\n';
    
    
    
    // begin(), end()
    cout << "traverse" << '\n';
    // map< string, int >::iterator it; also possible
    for(auto it = m.begin(); it != m.end(); it++){
        cout << "key : " << it->first << " " << "value : " << it->second << '\n';
    }
    
    return 0;
    
}
