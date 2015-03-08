Title: Building Hadoop 2.6 on 64-bit Windows 7
Date: 2015-03-08 20:30
Category: Tutorial
Authors: Suhas
Tags: Programming, Tutorial
Summary: Building Hadoop on Windows is a painful task. It has a zillion dependencies and the build almost always fails, but after a quadrillion tries...

### System

* Windows 7 Ultimate Service Pack 1
* Intel(R) Core(TM) i5-4210U CPU @ 1.70 GHz 1.70 GHz
* 8.00 GB RAM
* 64-bit Operating System

### Prerequisites

I'm going to assume that you have access to (and) know how to perform the below:

* Good Internet connection
* Admin account
* Ability to change Path variable and add new env variables
    - Click Start
    - Right click on Computer
    - Choose Properties
    - Click on Advanced system settings
    - Environment variables...

### Steps to build Hadoop 2.6

1. Download the 2.6 release from http://hadoop.apache.org/releases.html and extract it to somewhere with a short path like `C:\hdc\`
2. Go through the `BUILDING.txt` file
3. Download and install .NET framework 4.0 (*not* 4.5) from http://www.microsoft.com/en-in/download/details.aspx?id=17851
4. Download and install Windows SDK 7.1 from http://www.microsoft.com/en-in/download/details.aspx?id=8279
5. Download and install the latest JDK (I used Java 1.8 and it worked for me) and update your `JAVA_HOME` environment variable, add `%JAVA_HOME%\bin` to your path. (My `JAVA_HOME` is `C:\Java\jdk1.8.0_40`)
6. Download maven from http://maven.apache.org/download.cgi and extract it. Update the `M2_HOME` environment variable and add `%M2_HOME%\bin` to your path. (My `M2_HOME` is `C:\app\apache-maven-3.2.5`)
7. Download Findbugs 1.3.9 from http://sourceforge.net/projects/findbugs/files/findbugs/1.3.9/ and update `FINDBUGS_HOME` environment variable and add `%FINDBUGS_HOME%\bin` to your path
8. Download ProtocolBuffer 2.5.0 from https://code.google.com/p/protobuf/downloads/list (`protoc-2.5.0-win32.zip`) and add the extracted folder to your path
9. Download the latest CMAKE http://www.cmake.org/ and add it to your path 
10. Download Zlib source and DLL files from http://www.zlib.net/ and update `ZLIB_HOME` to the source file directory and add the DLL directory to your path
11. Download Cygwin and add it to your path (I've appended `C:\cygwin64\bin` instead of prepending to avoid some conflicts)
12. Add `Platform` environment variable and set it to `x64` and if you've read the `BUILDING.txt` file, it says that it must be "Platform", not "PLATFORM" or "platform"
13. Add `MSBuild.exe` folder location to your path, that's `C:\Windows\Microsoft.NET\Framework64\v4.0.30319`  
14. Goto Start > All Programs > Microsoft Windows SDK 7.1 > Windows SDK 7.1 Command Prompt > Right click > Open as administrator
15. Run the maven build command `mvn package -Pdist,native-win -Dmaven.javadoc.skip=true -DskipTests -Dtar` which is going to take a while... and if all goes well...

![Build successful]({filename}img\hadoopbuildsuccess.PNG)
