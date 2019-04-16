#include <algorithm>
#include <sys/time.h> // used only for Linux

/* //for Windows

#include <Windows.h>

SYSTEMTIME st;
GetSystemTime(&st);
// then convert st to your precision needs

*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
const int n1 = 50000,
          n2 =  100000,
          n3 =  500000,
          n4 =  1000000,
          n5 =  5000000,
          n6 =  10000000,
          n7 =  50000000,

          n = n1; // size of the file

double Arr[n];

double str2dbl(string S){
  return atof(S.c_str());
}

void outfile(){ //call this function in main if you want to create an output file
  ofstream file;
  file.open("output.txt");
  for (int i=0;i<n;i++){
    file << Arr[i] << '\n';
  }
}

int main() {
  ifstream file;
  string line;
  int i = 0;

  file.open("path.txt");
  while (getline(file,line))
    Arr[i++]=str2dbl(line);
  file.close();

  timeval start, final;
  gettimeofday(&start, 0);
  sort(begin(Arr),end(Arr));
  gettimeofday(&final,0);


  std::cout << (final.tv_sec - start.tv_sec + (double)(final.tv_usec)/1000000) - (double)(start.tv_usec)/1000000<<"s \n";
  //outfile();
  return 0;
}
