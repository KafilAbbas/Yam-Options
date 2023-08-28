import './table.css'


function NameList(props) {
    const mydata = props.mydata;
   if (mydata.length === 0)
   {
    return(
      <div className='default'>Please give some input</div>
    )
   }
   else
   {
    return (
      <div className= 'table_box'>
        <div >
            <table border={2} className='Table'>
              <thead>
                  <tr>
                    <th colSpan={5} style={{color: 'green'}}>CALL</th>
                    <th style={{color:'#4A4595'}}>Strike</th>
                    <th colSpan={5} style={{color:'red'}}>PUTS</th>
                      {/* {tableheading.map((label, index) => (
                          <th key={index} >{label}</th>
                      ))} */}
                  </tr>
              </thead>
              <tbody>
                      {mydata.map((rowdata, rowindex) => (
                        <tr key = {rowindex} >
                          {rowdata.map((cellData, cellIndex) => (
                          <td key={cellIndex}>{cellData}</td>
                        ))}
                        </tr>  
                      ))}
              </tbody>
          </table>
        </div>
        </div>
     );
    }
  }

  export default NameList;