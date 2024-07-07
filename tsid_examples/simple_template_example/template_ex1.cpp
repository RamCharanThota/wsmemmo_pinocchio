#include<iostream>

template <typename T>
void Foo(){

    std::cout << "Type of variable: " << typeid(T).name() << std::endl;

}

int main(){
    Foo<int> ();

    Foo<float>();

    return 0;
}