from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Board
from ..forms import BoardForm

@login_required(login_url='common:login')
def board_create(request, group):
    """
    Board 등록
    """
    # SubNav Active 처리 파라미터
    request.session.target_nav_item = 'bbs'

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.group = group
            board.author = request.user
            board.create_date = timezone.now()
            board.save()
            return redirect('board:list', group=group)
    else:
        form = BoardForm()
    context = {'form': form, 'group': group}
    return render(request, 'board/board_form.html', context)

@login_required(login_url='common:login')
def board_modify(request, board_id):
    """
    Board 수정
    """
    # SubNav Active 처리 파라미터
    request.session.target_nav_item = 'bbs'

    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', board_id=board.id)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.modify_date = timezone.now()  # 수정일시 저장
            board.save()
            return redirect('board:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form, 'group': board.group}
    return render(request, 'board/board_form.html', context)

@login_required(login_url='common:login')
def board_delete(request, board_id):
    """
    Board 삭제
    """
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', board_id=board.id)
    board.delete()
    return redirect('board:list', group=board.group)