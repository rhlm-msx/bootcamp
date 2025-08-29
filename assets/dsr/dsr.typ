#set text(size: 13pt, fill: black, font: "Montserrat")
#let dsr = yaml("dsr.yaml")
#set table.cell(inset: 7pt, align: horizon)

#{

show table.cell: cell => {
  if cell.x == 0 {
    strong(cell)
  }
  else{
   cell
  }
}
  table(
  columns: (1.8fr, 1fr, 1fr),
  fill: (x, y) => {
    if (x == 0){
      gray
    }
  },
  [Mentor], table.cell([#dsr.mentor], colspan: 2),
  [Code Reviewer], table.cell([NA], colspan: 2),
  [Bootcamp Progress Status], strong()[Week #dsr.week], text(fill: green, [GREEN]),

)
}

#show table.cell: (cell) => {
  if cell.y == 0{
    strong(cell)
  }
  else{
    cell
  }
}

#set table(fill: (x, y) => {
  if y == 0 {
    gray
  }
})


#set list(spacing: 0pt, tight: true)
#let create_lists(val) = {
  if type(val) == dictionary {
    
    return val.keys().map(key => {
      let cont = create_lists(val.at(key))
      list[#strong(key) #cont]
    }).join()
  }
  else if type(val) == array{
      return val.map(create_lists).join()
  }
  else{
    return list()[#val]
  }
}



#table(
  columns: (2fr, 1fr),
  align: horizon,
  table.header([Status Report:[#datetime.today().display("[month repr:short] [day], [year]")]], [Status]),
  ..for i in range(dsr.report.len()){
  (create_lists(dsr.report.at(i)),
  dsr.rep-status.at(i))
}
)


#table(
  columns: (2fr, 1fr),
  [Challenges Faced], [Status],
  ..for i in range(dsr.challenges.len()){
  (create_lists(dsr.challenges.at(i)),
  dsr.challenges-status.at(i))
}
)

#table(
  columns: 1fr,
  [Resolution for Challenges],
  ..dsr.resolution.map(create_lists)
)


#show link:it => {
  set text(blue, font: "Ubuntu")
  underline(it)
}
#table(
  columns: 1fr,
  [References],
  ..range(dsr.references.len()).map(i => dsr.references.at(i).keys().map(key => link(dsr.references.at(i).at(key))[#key]).at(0))
)


#table(
  columns: 1fr,
  [Code Commit Link],
  if dsr.commits != none {
  for i in range(dsr.commits.len()){
  dsr.commits.at(i).keys().map(key => link(dsr.commits.at(i).at(key))[#key]).at(0)
}
}
)

#table(
  columns: 1fr,
  table.header([Next day plan: [#(datetime.today() + duration(days: 1)).display("[month repr:short] [day], [year]")]]),
  ..dsr.next.map(create_lists)
)

