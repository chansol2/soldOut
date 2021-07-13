import React from 'react'
import Product from './Product'
import classes from './ProductList.module.css'

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

function ProductList(props) {
    return (
        <div className={classes.container}>
            <div className={classes.title}>수정이 필요한 상품 리스트</div>
            <div className={classes.productList}>
            {props.loadedProducts.map((prd) => (
                <Product key={prd.id} prd={prd.data} />
            ))}
            </div>
        </div>
    )
}

export default ProductList
