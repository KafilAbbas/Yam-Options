function NameList(props) {
    const mydata = props.mydata;
   if (mydata.length === 0)
   {
    return(
      <div>please give some input</div>
    )
   }
   else
   {
    return (
        <div>
            <table border={2}>
              <thead>
                  <tr>
                    <th colSpan={5}>CALL</th>
                    <th>Strike</th>
                    <th colSpan={5}>PUTS</th>
                      {/* {tableheading.map((label, index) => (
                          <th key={index} >{label}</th>
                      ))} */}
                  </tr>
              </thead>
              <tbody>
                      {mydata.map((rowdata, rowindex) => (
                        <tr key = {rowindex}>
                          {rowdata.map((cellData, cellIndex) => (
                          <td key={cellIndex}>{cellData}</td>
                        ))}
                        </tr>  
                      ))}
              </tbody>
          </table>
        </div>
     );
    }
  }

  export default NameList;