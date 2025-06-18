//
//  main.swift
//  SortingAlgsSwift
//
//  Created by Will Gibson on 1/29/24.
//

import Foundation

print("Hello, World!")

func bubbleSort(list: [Int]){
    var tmp = list
    let start = CFAbsoluteTimeGetCurrent()
    var temp: Int
    for _ in 0..<list.count-1{
        for j in 0..<list.count-1{
            if list[j] > list[j+1]{
                temp = tmp[j]
                tmp[j] = tmp[j+1]
                tmp[j+1] = temp
            }
        }
    }
    let diff = CFAbsoluteTimeGetCurrent() - start
    print(diff)
}

func insertionSort(list array: [Int]) {
    var tmp = array
    let start = CFAbsoluteTimeGetCurrent()
    for x in 1..<array.count {
        var y = x
        while y > 0 && array[y] < array[y - 1] {
            tmp.swapAt(y, y - 1)
            y -= 1
        }
    }
    var diff = CFAbsoluteTimeGetCurrent() - start
    print(diff)
}


func mergeSort(_ array: [Int]) -> [Int] {
    
    guard array.count > 1 else { return array }

    let middleIndex = array.count / 2
    let leftArray = mergeSort(Array(array[..<middleIndex]))
    let rightArray = mergeSort(Array(array[middleIndex...]))

    return merge(leftArray, rightArray)
}

func merge(_ left: [Int], _ right: [Int]) -> [Int] {
    var leftIndex = 0
    var rightIndex = 0
    var sortedArray: [Int] = []

    while leftIndex < left.count && rightIndex < right.count {
        if left[leftIndex] < right[rightIndex] {
            sortedArray.append(left[leftIndex])
            leftIndex += 1
        } else {
            sortedArray.append(right[rightIndex])
            rightIndex += 1
        }
    }

    while leftIndex < left.count {
        sortedArray.append(left[leftIndex])
        leftIndex += 1
    }

    while rightIndex < right.count {
        sortedArray.append(right[rightIndex])
        rightIndex += 1
    }

    return sortedArray
}


func readArrayFromFile(at path: String) -> [Int]? {
    do {
        // Read the contents of the file
        let contents = try String(contentsOfFile: path, encoding: .utf8)
        // Split the contents into an array of strings, one for each number
        let strings = contents.split(separator: " ").map(String.init)
        // Convert the array of strings to an array of integers
        let numbers = strings.compactMap { Int($0.trimmingCharacters(in: .whitespacesAndNewlines)) }
        return numbers
    } catch {
        print("Error reading file: \(error)")
        return nil
    }
}

let fileNames: [String] = ["SortedRandomNumbersSmall",
                           "RandomNumbersSmall",
                           "ReversedRandomNumbersSmall",
                           "SortedRandomNumbersLarge",
                           "RandomNumbersLarge",
                           "ReversedRandomNumbersLarge"]


func readFromArrays(array: [String]){
    
    for elem in array {
        // Example usage
        if let path = Bundle.main.path(forResource: elem, ofType: "txt", inDirectory: "Data") {
            if let numbers = readArrayFromFile(at: path) {
                print("File Started \(elem)")
                print("Bubble Sort")
                bubbleSort(list: numbers)
                print("")
                print("InsertionSort")
                insertionSort(list: numbers)
                print("")
                print("Merge Sort")
                let start = CFAbsoluteTimeGetCurrent()
                var _ = mergeSort(numbers)
                let diff = CFAbsoluteTimeGetCurrent() - start
                print(diff)
                
            }
        }
    }
}

readFromArrays(array: fileNames)
