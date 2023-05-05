from typing import List, Annotated
from app import dto, services, core, entity
from fastapi import APIRouter, Depends, status, HTTPException, Form
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[dto.Server])
async def get_all_servers(
    deployer: str = None,
    exclude_deployer: str = None,
    db: Session = Depends(core.get_db),
) -> List[entity.ServerEntity]:
    if deployer and exclude_deployer:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="You cannot set deployer and exclude_deployer at the saem time",
        )

    if deployer:
        server = dto.Server(server_deployer=deployer)
        return services.server.get_by_deployer(db=db, server=server)
    if exclude_deployer:
        server = dto.Server(server_deployer=exclude_deployer)
        return services.server.get_except_deployer(db=db, server=server)

    return services.server.get_all(db=db)


@router.get("/{server_name}", status_code=status.HTTP_200_OK, response_model=dto.Server)
async def get_one_server(
    server_name: str,
    db: Session = Depends(core.get_db),
) -> entity.ServerEntity:
    server_in = dto.Server(server_name=server_name)
    server = services.server.get(db=db, server=server_in)
    if server is None:
        return dto.Server()
    else:
        return server


@router.get(
    "/{server_name}/status",
    status_code=status.HTTP_200_OK,
    # response_model=dto.ServerStatus,
)
async def get_server_status(
    server_name: str, db: Session = Depends(core.get_db)
) -> dto.ServerStatus:
    server_in = dto.Server(server_name=server_name)
    server_db_obj = services.server.get(db=db, server=server_in)
    server = dto.Server.from_orm(server_db_obj)

    s = services.kube.get_server_status(server)
    return s


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_server(
    server_name: Annotated[str, Form()],
    server_description: Annotated[str, Form()],
    server_deployer: Annotated[str, Form()],
    game_server_tag: Annotated[str, Form()],
    macaron_tag: Annotated[str, Form()],
    db: Session = Depends(core.get_db),
) -> dto.Server:
    server_in = dto.Server(
        server_name="gb-" + server_name,
        description=server_description,
        server_deployer=server_deployer,
        game_server_tag=game_server_tag,
        macaron_tag=macaron_tag,
    )
    services.server.create(db=db, server=server_in)
    return RedirectResponse("/dashboard", status_code=status.HTTP_302_FOUND)


@router.delete(
    "/{server_name}", status_code=status.HTTP_200_OK, response_model=dto.Server
)
async def delete_server(
    server_name: str, db: Session = Depends(core.get_db)
) -> dto.Server:
    server_in = dto.Server(server_name=server_name)
    return services.server.delete(db=db, server=server_in)


@router.delete(
    "/{server_name}/kube", status_code=status.HTTP_200_OK, response_model=dto.Server
)
async def delete_server(
    server_name: str, db: Session = Depends(core.get_db)
) -> dto.Server:
    server_in = dto.Server(server_name=server_name)
    services.kube.delete(server_in)
    return services.server.get(db=db, server=server_in)
