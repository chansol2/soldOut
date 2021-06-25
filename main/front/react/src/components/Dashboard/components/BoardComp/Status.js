import { useState } from "react";

import classes from "./Status.module.css";
import Product from "./Product";

const Status = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [loadedProducts, setLoadedProducts] = useState([]);
  const [loadedNumb, setLoadedNumb] = useState(0);

  const clickHandler = (e) => {
    // e.preventDefault();
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
    <div>
      {isLoading && <h1>is loading...</h1>}
      {!isLoading && (
        <div className={classes.container}>
          <div className={classes.cardOne}>
            <div className={classes.upper}>
              <div>
                <img alt="" />
              </div>
              <div>
                <div>2021.06.17.09:00시</div>
                <div>상품 업데이트를 완료했습니다.</div>
              </div>
            </div>
            <div className={classes.lower}>상품 업데이트 확인판</div>
          </div>
          <div className={classes.cardTwo}>
            <div className={classes.upper}>
              <strong>{loadedNumb}</strong>개 상품 수정 필요
            </div>
            <div className={classes.lower}>수정 필요 확인판</div>
          </div>
          <div className={classes.buttonContainer}>
            <div>
              <button onClick={clickHandler}>
                <img alt="" />
              </button>
              <div className={classes.text}>업데이트</div>
            </div>
          </div>
        </div>
      )}
      <div className={classes.containerPL}>
        <div className={classes.title}>수정이 필요한 상품 리스트</div>
        <div className={classes.productList}>
          {loadedProducts.map((prd) => (
            <Product key={prd.id} prd={prd.data} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Status;
