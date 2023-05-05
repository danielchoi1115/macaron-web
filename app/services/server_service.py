from typing import List
from app import dto, dao, entity, services
from sqlalchemy.orm import Session


class ServerService:
    def get(self, db: Session, server: dto.Server) -> entity.ServerEntity:
        return dao.server.select(db=db, dto=server)

    def get_all(self, db: Session) -> List[entity.ServerEntity]:
        return dao.server.select_all(db=db)

    def get_by_deployer(
        self, db: Session, server: dto.Server
    ) -> List[entity.ServerEntity]:
        return dao.server.select_by_deployer(db=db, dto=server)

    def get_except_deployer(
        self, db: Session, server: dto.Server
    ) -> List[entity.ServerEntity]:
        return dao.server.select_except_deployer(db=db, dto=server)

    def create(self, db: Session, server: dto.Server) -> entity.ServerEntity:
        # 0. domain name 결정
        # 1. flask deployment, service, ingress 생성 api 호출
        # 2. mysql deployment, service, ingress 생성 api 호출
        # 3. 중간에 하나라도 잘못된다면 revert
        # 4. 1초에 한 번씩 업데이트 후 경과 확인
        # 5. 전부 성공했다면 mysql 데이터베이스에 서버 메타정보 추가
        # 6.

        server_obj = dao.server.insert(db=db, dto=server)
        dao.server.commit(db)

        services.kube.create(server)

        return server_obj

    def update(self, db: Session, server: dto.Server) -> entity.ServerEntity:
        ...

    def delete(self, db: Session, server: dto.Server) -> entity.ServerEntity:
        server_obj = dao.server.delete(db=db, dto=server)
        dao.server.commit(db)
        return server_obj


server = ServerService()
