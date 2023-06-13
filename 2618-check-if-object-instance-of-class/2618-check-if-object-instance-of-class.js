/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
  if (obj === null || obj === undefined || classFunction === null || classFunction === undefined) {
      return false;
  }
  if (typeof classFunction !== 'function') {
    return false;
  }
  if (obj instanceof classFunction) {
    return true;
  }
  let proto = Object.getPrototypeOf(obj);
  while (proto) {
    if (proto.constructor === classFunction) {
      return true;
    }
    proto = Object.getPrototypeOf(proto);
  }
  return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */