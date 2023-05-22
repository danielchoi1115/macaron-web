# 마카롱맛 프로젝트

NDC17에서 발표된 오승용 개발자님의 [Kubernetes로 개발서버 간단히 찍어내기](https://www.slideshare.net/seungyongoh3/ndc17-kubernetes)를 보고 흥미가 생겨 일부 따라 구현해본 프로젝트입니다.

관리자 대시보드에서 서버를 클릭 한 번으로 간편하게 생성하거나 삭제할 수 있습니다.

그렇게 생성된 서버에는 서브도메인 주소가 자동으로 할당되어, 서버에서 작동중인 서비스에 손쉽게 접근할 수도 있습니다.

<img src="https://github.com/danielchoi1115/macaron-web/assets/100273844/37857d6c-d714-46d2-960a-f32ca2052b4e" width="700"/>


# 프로젝트 과정에서 얻고자 하는 것

1. 쿠버네티스 맛보기 (활용능력 습득하기)
2. 서버 환경 생성 자동화에 대한 흥미 해소


# 구현한 항목

1. 서버 생성과 삭제의 간편화
2. Ingress를 활용한 동적 서브도메인 생성기능
3. 생성된 서버의 메타정보를 확인할 수 있는 대시보드


# 참고자료

**시연영상 유튜브 링크**

[https://www.youtube.com/watch?v=XeAOgATG0aU](https://www.youtube.com/watch?v=XeAOgATG0aU)

**구현과정 상세 소개 PDF**

[https://github.com/danielchoi1115/macaron-web/blob/master/마카롱맛_프로젝트.pdf](https://github.com/danielchoi1115/macaron-web/blob/master/%EB%A7%88%EC%B9%B4%EB%A1%B1%EB%A7%9B_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8.pdf)