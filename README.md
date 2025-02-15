# 📚 Library Management System

## 🏛️ Welcome to the Library Management System

This is a simple **Python-based Library Management System** that allows users to explore a collection of books across different categories. It provides an interactive interface where users can select book categories and get details about available books.

## 🚀 Features

✅ **Interactive Console Interface** – Easy to navigate 📟  
✅ **Multiple Book Categories** – Programming, Data Science, Business, etc. 📖  
✅ **Auto-Recursive Selection** – Allows re-exploration 🔄  
✅ **User-Friendly Experience** – Simple and intuitive ⚡

## 🔧 How It Works

1️⃣ Run the program, and you will be greeted with a **welcome message**.  
2️⃣ Choose an option:
   - Press **1** to explore the library 📚
   - Press **2** to exit ❌
3️⃣ If you choose to explore, select a category:  
   - **1** – Programming 🖥️  
   - **2** – Data Science / Business 📊  
   - **3** – Business / Entrepreneurship 💼  
   - **4** – Software Development 💻  
   - **5** – Self-Help / Productivity 🌟  
4️⃣ Get book details (Name, Code, Edition).  
5️⃣ You can explore again or exit. 🔄

## 📜 Code Overview

```python
# Function to manage library

def library():
    a = int(input('Press 1 to explore library\nPress 2 to exit\n'))
    if a == 2:
        print('Thanks for visiting!')
    elif a == 1:
        b = int(input('For Programming press 1\nFor Data Science / Business press 2\nFor Business / Entrepreneurship press 3\nFor Software Development press 4\nFor Self-Help / Productivity press 5\n'))
        if b == 1:
            print('Book code 101\nName: Python Crash Course\nEdition: 2016')
        elif b == 2:
            print('Book code 102\nName: Data Science for Business\nEdition: 2012')
        elif b == 3:
            print('Book code 103\nName: The Lean Startup\nEdition: 2023')
        elif b == 4:
            print('Book code 104\nName: The Pragmatic Programmer\nEdition: 2024')
        elif b == 5:
            print('Book code 105\nName: Atomic Habits\nEdition: 2010')
        return library()
    else:
        print('Invalid input! Please try again.')
        return library()

print('Welcome to the Library Management System')
library()
```

## 🎯 Future Enhancements

🔹 **Book Availability Check** 📌  
🔹 **Borrow & Return Feature** 📖  
🔹 **Graphical User Interface (GUI) Support** 🖥️  

## 🤝 Contribute

If you want to improve this project, feel free to **fork**, **clone**, and submit a **pull request**! 🚀

## 📩 Let's Connect!

💼 **LinkedIn** – [Kartik Singh Chauhan](https://www.linkedin.com/in/kartik-chauhan-linkdin/)  
📧 **Email** – kartikrajput4466@gmail.com  


---

⭐ **If you like this project, don't forget to star it!** ⭐

