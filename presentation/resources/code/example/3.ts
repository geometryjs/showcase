import * as GeometryJS from '@jiricekcz/geometry.js';

const plane = GeometryJS.createPlane();

const x = plane.createValue(1);
const y = plane.createReadonlyValue(2);

const A = plane.createPointFromTwoValues(x, y);
const B = plane.createPointFromCoordinates(3, 4);





