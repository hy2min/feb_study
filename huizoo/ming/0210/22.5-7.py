arr = [
    [[' ','#',' '],
     ['#',' ','#'],
     ['#','#','#'],
     ['#',' ','#'],
     ['#',' ','#']],
    [['#','#','#'],
     ['#',' ','#'],
     ['#','#','#'],
     ['#',' ','#'],
     ['#','#','#']],
    [['#','#','#'],
     ['#',' ','#'],
     ['#',' ',' '],
     ['#',' ','#'],
     ['#','#','#']],
    [['#','#',' '],
     ['#',' ','#'],
     ['#',' ','#'],
     ['#',' ','#'],
     ['#','#',' ']],
]

n = int(input())
print('\n'.join(''.join(row) for row in arr[n]))