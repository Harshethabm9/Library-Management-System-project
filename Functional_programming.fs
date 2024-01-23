type Library = {
    Books: string list
}

let displayAvailableBooks (library: Library) =
    printfn "\n%d AVAILABLE BOOKS ARE:" (List.length library.Books)
    library.Books |> List.iter (fun book -> printf " ♦-- %s\n" book)
    printfn "\n"

let borrowBook (name: string) (bookname: string) (library: Library) =
    match List.contains bookname library.Books with
    | false -> sprintf "%s BOOK IS NOT AVAILABLE OR TAKEN BY SOMEONE ELSE." bookname, library
    | true ->
        let updatedBooks = library.Books |> List.filter (fun b -> b <> bookname)
        sprintf "BOOK ISSUED! THANK YOU, %s." name, { library with Books = updatedBooks }

let returnBook (bookname: string) (library: Library) =
    sprintf "BOOK RETURNED! THANK YOU!" , { library with Books = bookname :: library.Books }

let donateBook (bookname: string) (library: Library) =
    sprintf "BOOK DONATED! THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD." , { library with Books = bookname :: library.Books }

let rec main library issuedBooks =
    printfn "\nWELCOME TO THE FUNCTIONAL LIBRARY MANAGEMENT SYSTEM\n"

    let getUserInput prompt =
        printfn "%s" prompt
        System.Console.ReadLine()

    printfn """CHOOSE WHAT YOU WANT TO DO:
        1. Show Listing of all books
        2. Borrow a book
        3. Return a book
        4. Donate a book
        5. Track Books
        6. Exit the library"""

    try
        let userResponse = int (getUserInput "Enter your choice: ")

        match userResponse with
        | 1 ->
            displayAvailableBooks library
            main library issuedBooks

        | 2 ->
            let name = getUserInput "Enter your name: "
            let book = getUserInput "Enter the name of the book you want to borrow: "
            let result, updatedLibrary = borrowBook name book library
            printfn "%s\n" result
            main updatedLibrary (issuedBooks @ [{name = name; book = book}])

        | 3 ->
            let book = getUserInput "Enter the name of the book you want to return: "
            let result, updatedLibrary = returnBook book library
            printfn "%s\n" result
            main updatedLibrary (List.filter (fun record -> record.book <> book) issuedBooks)

        | 4 ->
            let book = getUserInput "Enter the name of the book you want to donate: "
            let result, updatedLibrary = donateBook book library
            printfn "%s\n" result
            main updatedLibrary issuedBooks

        | 5 ->
            issuedBooks |> List.iter (fun record -> printfn "%s book is taken/issued by %s." record.book record.name)
            printfn ""
            if List.isEmpty issuedBooks then printfn "NO BOOKS ARE ISSUED!\n"
            main library issuedBooks

        | 6 ->
            printfn "THANK YOU!\n"
            exit 0

        | _ ->
            printfn "INVALID INPUT!\n"
            main library issuedBooks

    with
    | :? System.FormatException ->
        printfn "INVALID INPUT!\n"
        main library issuedBooks

let initialLibrary = { Books = ["Vistas"; "Invention"; "Rich & Poor"; "Indian"; "Macroeconomics"; "Microeconomics"] }
let initialIssuedBooks = []

main initialLibrary initialIssuedBooks

