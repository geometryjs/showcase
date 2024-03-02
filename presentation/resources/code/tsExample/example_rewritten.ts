function filter<T>(array: Array<T>, predicate: (value: T) => boolean): Array<T> {
    var result: Array<T> = [];
    for (var i = 0; i < array.length; i++) {
        if (predicate(array[i])) {
            result.push(array[i])
        }
    }
    return result;
}