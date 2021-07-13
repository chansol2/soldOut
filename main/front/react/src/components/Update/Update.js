import classes from "./Update.module.css";
import Status from "./Status";
import ProductList from "./ProductList";
import { useState } from "react";

const Update = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [loadedProducts, setLoadedProducts] = useState([]);
  const [loadedNumb, setLoadedNumb] = useState(0);

  const clickHandler = (e) => {
    setIsLoading(true);
    //sending a get request to localhost:5000
    fetch("http://localhost:5000/update")
      .then((res) => {
        setIsLoading(false);
        if (res.ok) {
          return res.json();
        } else {
          setIsLoading(true);
          alert("sth went wrong");
          return res.json().then((data) => {
            throw new Error(data ? data.description : "fuck, it's an error");
          });
        }
      })
      .then((data) => {
        setLoadedProducts(data);
        setLoadedNumb(data.length);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div className={classes.container}>
      <Status onClickUpdate={clickHandler} isLoading={isLoading} loadedNumb={loadedNumb}/>
      <ProductList loadedProducts={loadedProducts}/>
    </div>
  );
};

export default Update;
