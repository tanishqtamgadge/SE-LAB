#include<iostream>
using namespace std;
class complex
{
    float x;
    float y;
    public:
    complex():x(0),y(0)
    {}
    complex operator+(const complex&c)const;
    complex operator*(const complex&c)const;

    friend istream&operator>>(istream&input,complex&t)
    {
        input>>t.x;
        input>>t.y;
    }
    friend ostream&operator>>(ostream&output,complex&t)
    {
       output<<t.x<<"+"<<t.y<<"i";
    }
};
    complex complex::operator+(const complex&c)const
    {
        complex temp;
        temp.x = x + c.x;
        temp.y = y + c.y;
        return temp;
    }
    complex complex:: operator*(const complex&c)const
    {
        complex temp;
       temp.x = x*c.x - y*c.y;
        temp.y = y*c.y + x*c.x;
        return temp;
    }

int main()
{
    complex c1,c2,c3,c4;
    cout<<"Enter the first complex part:";
    cin>>c1;
    cout<<"Enter the second complex part:";
    cin>>c2;
    c3=c1+c2;
    c4=c1*c2;
    cout<<"First complex number:" <<c1<<endl;
    cout<<"Second complex number:" <<c2<<endl;
    cout<<"Sum:" <<c3<<endl;
    cout<<"Product:" <<c4<<endl;
    return 0;
}