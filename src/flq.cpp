/*
    File lines to quoted lines
    An utility to prepare string variables intialization multiple string values.
*/

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

string help_message = " Usage: \n"
                                   "        flq filename\n";

string error_message = " Something went wrong.\n";

int main(int argc, char *argv[])
{
    string file_name = "";

    if (argc < 2)
    {
        printf("\n%s\n", help_message.c_str());
        return 0;
    }
    else
    {
        file_name = argv[1];
    }

    ifstream the_file(file_name);
    if (!the_file.is_open())
    {
        printf("\n Opening '%s': %s\n", file_name.c_str(), error_message.c_str());
        return 0;
    }

    string the_buffer;

    while (getline(the_file, the_buffer))
    {
        if (the_buffer.length() > 0)
        {
            cout << "\"" << the_buffer << "\"\n";
        }
        else
        {
            cout << "\n";
        }
    }

    the_file.close();

    return 0;
}