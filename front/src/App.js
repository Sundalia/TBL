import React, {useEffect, useState} from 'react';
import './App.css';
import data from './bridge.json'

// Во фронте я реализовала, худо-бедно, только вывод, оправдываться не буду, 
// не обессудьте, спасибо, хорошего дня!
function App() {

  const [rows, setRows] = useState(data);

  return (
    <div className="app-container">
       <table>
         <thead>
           <tr>
              <th>Дата</th>
              <th>Название</th>
              <th>Номер</th>
              <th>Расстояние</th>
           </tr>
         </thead>
         <tbody>
            {rows.map((row) => (
            <><tr>
                <td class='one'>{row[0]}</td>
                <td>{row[1]}</td>
                <td class='one'>{row[2]}</td>
                <td>{row[3]}</td>
              </tr></>
          ))}
          </tbody>
        </table>
    </div>
  );
}

export default App;