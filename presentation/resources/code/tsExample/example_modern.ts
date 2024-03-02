function filter<T>(array: Array<T>, predicate: (item: T) => boolean): Array<T> {
    const result: Array<T> = [];
    for (const item of array) {
        if (predicate(item)) {
            result.push(item)
        }
    }
    return result;
}