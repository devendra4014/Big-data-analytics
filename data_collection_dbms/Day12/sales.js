
db.customers.drop();
db.salespeople.drop();
db.orders.drop();

db.customers.insert({ _id: 2001, name: 'Hoffman', city: 'London', rating: 100, snum: 1001});
db.customers.insert({ _id: 2002, name: 'Giovanni', city: 'Rome', rating: 200, snum: 1003});
db.customers.insert({ _id: 2003, name: 'Liu', city: 'San Jose', rating: 200, snum: 1002});
db.customers.insert({ _id: 2004, name: 'Grass', city: 'Berlin', rating: 300, snum: 1002});
db.customers.insert({ _id: 2006, name: 'Clemens', city: 'London', rating: 100, snum: 1001});
db.customers.insert({ _id: 2008, name: 'Cisneros', city: 'San Jose', rating: 300, snum: 1007});
db.customers.insert({ _id: 2007, name: 'Pereira', city: 'Rome', rating: 100, snum: 1004});

db.salespeople.insert({ _id: 1001, sname: 'Peel', city: 'London', comm: 0.12});
db.salespeople.insert({ _id: 1002, sname: 'Serres', city: 'San Jose', comm: 0.13});
db.salespeople.insert({ _id: 1004, sname: 'Motika', city: 'London', comm: 0.11});
db.salespeople.insert({ _id: 1007, sname: 'Rifkin', city: 'Barcelona', comm: 0.15});
db.salespeople.insert({ _id: 1003, sname: 'Axelrod', city: 'New York', comm: 0.10});

db.orders.insert({ _id: 3001, amt: 18.69, odate: '1990-10-03', cnum: 2008, snum: 1007});
db.orders.insert({ _id: 3003, amt: 767.19, odate: '1990-10-03', cnum: 2001, snum: 1001});
db.orders.insert({ _id: 3002, amt: 1900.10, odate: '1990-10-03', cnum: 2007, snum: 1004});
db.orders.insert({ _id: 3005, amt: 5160.45, odate: '1990-10-03', cnum: 2003, snum: 1002});
db.orders.insert({ _id: 3006, amt: 1098.16, odate: '1990-10-03', cnum: 2008, snum: 1007});
db.orders.insert({ _id: 3009, amt: 1713.23, odate: '1990-10-04', cnum: 2002, snum: 1003});
db.orders.insert({ _id: 3007, amt: 75.75, odate: '1990-10-04', cnum: 2004, snum: 1002});
db.orders.insert({ _id: 3008, amt: 4723.00, odate: '1990-10-04', cnum: 2006, snum: 1001});
db.orders.insert({ _id: 3010, amt: 309.95, odate: '1990-10-04', cnum: 2004, snum: 1002});
db.orders.insert({ _id: 3011, amt: 9891.88, odate: '1990-10-04', cnum: 2006, snum: 1001});
