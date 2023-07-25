db.students.insert({
    _id: 1,
    name: 'Sachin',
    hobbies: ['Programming', 'Teaching'],
    academics: [
      {
        std: '10th',
        passing: 1998,
        marks: 78.66,
      },
      {
        std: '12th',
        passing: 2000,
        marks: 77.0,
      },
      {
        std: 'B.Sc.',
        passing: 2004,
        marks: 60.0,
      },
      {
        std: 'M.Sc.',
        passing: 2008,
        marks: 59.2,
      },
    ],
  })
  
  db.students.insert({
    _id: 2,
    name: 'Sameer',
    hobbies: ['Programming'],
    academics: [
      {
        std: '10th',
        passing: 1998,
        marks: 98.0,
      },
      {
        std: '12th',
        passing: 2000,
        marks: 94.0,
      },
      {
        std: 'B.E.',
        passing: 2004,
        marks: 75.0,
      },
    ],
  })
  
  db.students.insert({
    _id: 3,
    name: 'Dinesh',
    hobbies: ['Music', 'Sports', 'Drawing'],
    academics: [
      {
        std: '10th',
        passing: 2004,
        marks: 65.0,
      },
      {
        std: '12th',
        passing: 2006,
        marks: 64.0,
      },
      {
        std: 'B.A.',
        passing: 2009,
        marks: 60.0,
      },
    ],
  })

  
