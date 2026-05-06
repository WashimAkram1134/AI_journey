# Python Essentials Part 2 — Real Data Handling (May 6)

## 1. What is JSON?
JSON (JavaScript Object Notation) is a structured text format used to store and exchange labeled data between systems. APIs, AI models, and web apps commonly communicate using JSON.

## 2. Difference Between JSON and Python Dictionary
Python dictionary is an internal Python object stored in memory.
JSON is a text-based communication/storage format.
Python converts dictionary to JSON using json.dump/json.dumps.

## 3. What is json.dump()?
json.dump() writes Python dictionary data into a file in JSON format.

Example:
json.dump(user_data, file, indent=4)

## 4. Why List of Dictionaries Matters
Multiple user records, document chunks, search results, and AI metadata are often stored as list of dictionaries.

## 5. Why Error Handling Matters
Production AI apps can fail because of bad input, API failure, invalid file, or zero results.
try/except prevents the full application from crashing.

## 6. Why Modular Coding Matters
Functions in separate files make code reusable, cleaner, and scalable.

## 7. Today's Key Learning
- JSON is machine communication language
- Dictionary and JSON are not exactly same
- json.dump saves data externally
- try/except makes apps safer
- utils.py creates reusable logic