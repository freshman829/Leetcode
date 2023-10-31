/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    const stack = [];

    for (const asteroid of asteroids) {
        let survived = true;

        while (stack.length > 0 && stack[stack.length - 1] > 0 && asteroid < 0) {
            const prevAsteroid = stack.pop();
            const collisionResult = prevAsteroid + asteroid;

            if (collisionResult > 0) {
                stack.push(prevAsteroid);
                survived = false;
                break;
            } else if (collisionResult === 0) {
                survived = false;
                break;
            }
        }

        if (survived) {
            stack.push(asteroid);
        }
    }

    return stack;
};

