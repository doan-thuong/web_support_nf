export function ColorOfStatus(status) {
    var color

    switch (status) {
        case -1:
            color = "Black"

            break
        case 0:
            color = "Green"

            break
        case 1:
            color = "Yellow"

            break
        case 2:
            color = "Purple"

            break
        case 3:
            color = "Gray"

            break
        case 4:
            color = "Red"

            break
        default:
            color = "Black"
    }

    return color
}