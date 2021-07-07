import { useState } from "react";

import classes from "./Status.module.css";
import Product from "./Product";

const Status = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [loadedProducts, setLoadedProducts] = useState([]);
  const [loadedNumb, setLoadedNumb] = useState(0);

  const Dummy = [
    {
      "id": 1,
      "data": {
        "prd_id": 1,
        "seller_nm": "지마켓",
        "prd_nm": "가구가구가구",
        "org_url": "www.google.com",
        "sales_price": "22,000",
        "has_Stock": false
      }
    },
    {
      "id": 2,
      "data": {
        "prd_id": 2,
        "seller_nm": "쿠팡",
        "prd_nm": "가구가구가구",
        "org_url": "www.facebook.com",
        "sales_price": "29,000",
        "has_Stock": false
      }
    },
    {
      "id": 3,
      "data": {
        "prd_id": 3,
        "seller_nm": "SSG",
        "prd_nm": "가구가구가구",
        "org_url": "www.apple.com",
        "sales_price": "24,000",
        "has_Stock": false
      }
    },
    {
      "id": 4,
      "data": {
        "prd_id": 4,
        "seller_nm": "오늘의집",
        "prd_nm": "가구가구가구",
        "org_url": "www.instagram.com",
        "sales_price": "21,000",
        "has_Stock": false
      }
    }
  ]

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
          {Dummy.map((prd) => (
            <Product key={prd.id} prd={prd.data} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Status;
